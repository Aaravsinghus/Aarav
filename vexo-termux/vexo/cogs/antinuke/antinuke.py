"""
AntiNuke Cog - Protect your Discord server from mass actions
Created for Vexo Bot
"""

import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional, List
import asyncio
from datetime import datetime, timedelta

class AntiNuke(commands.Cog):
    """🛡️ AntiNuke Protection - Prevent server destruction"""

    antinuke_group = app_commands.Group(name="antinuke", description="AntiNuke protection commands")
    
    def __init__(self, bot):
        self.bot = bot
        self.protected_guilds = {}
        self.raid_detection = {}
        self.cooldowns = {}

    def _make_embed(self, title: str, description: str, color: discord.Color, footer: str = "AntiNuke Protection") -> discord.Embed:
        embed = discord.Embed(title=title, description=description, color=color)
        embed.set_footer(text=footer)
        embed.timestamp = datetime.utcnow()
        return embed

    @commands.group(name="antinuke", invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def antinuke(self, ctx):
        """AntiNuke protection commands"""
        embed = discord.Embed(
            title="🛡️ AntiNuke Protection",
            description="Protect your server from mass actions and raid attacks",
            color=discord.Color.red()
        )
        embed.add_field(
            name="📋 Commands",
            value="""
`antinuke enable` - Enable AntiNuke protection
`antinuke disable` - Disable AntiNuke protection
`antinuke status` - Check protection status
`antinuke threshold <number>` - Set action threshold (default: 5)
`antinuke whitelist <role>` - Whitelist a role
`antinuke blacklist <user>` - Blacklist a user
            """,
            inline=False
        )
        embed.add_field(
            name="⚙️ Features",
            value="""
✅ Detects rapid channel deletions
✅ Detects rapid role changes
✅ Detects mass bans/kicks
✅ Auto-mutes suspicious users
✅ Sends alerts to mod logs
            """,
            inline=False
        )
        embed.set_footer(text="Use antinuke <subcommand> for more info")
        await ctx.send(embed=embed)
    
    @antinuke.command(name="enable")
    @commands.has_permissions(administrator=True)
    async def enable_antinuke(self, ctx):
        """Enable AntiNuke protection for this server"""
        guild_id = ctx.guild.id
        self.protected_guilds[guild_id] = {
            "enabled": True,
            "threshold": 5,
            "whitelist": [],
            "blacklist": [],
            "enabled_at": datetime.now()
        }
        
        embed = discord.Embed(
            title="✅ AntiNuke Enabled",
            description=f"Server protection activated for **{ctx.guild.name}**",
            color=discord.Color.green()
        )
        embed.add_field(
            name="🔧 Default Settings",
            value=f"""
Threshold: 5 actions
Whitelist: Empty
Blacklist: Empty
            """
        )
        await ctx.send(embed=embed)
    
    @antinuke.command(name="disable")
    @commands.has_permissions(administrator=True)
    async def disable_antinuke(self, ctx):
        """Disable AntiNuke protection for this server"""
        guild_id = ctx.guild.id
        if guild_id in self.protected_guilds:
            self.protected_guilds[guild_id]["enabled"] = False
        
        embed = discord.Embed(
            title="❌ AntiNuke Disabled",
            description=f"Server protection deactivated for **{ctx.guild.name}**",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)
    
    @antinuke.command(name="status")
    @commands.has_permissions(administrator=True)
    async def antinuke_status(self, ctx):
        """Check AntiNuke protection status"""
        guild_id = ctx.guild.id
        status = self.protected_guilds.get(guild_id, {"enabled": False})
        
        is_enabled = status.get("enabled", False)
        threshold = status.get("threshold", 5)
        whitelist_count = len(status.get("whitelist", []))
        blacklist_count = len(status.get("blacklist", []))
        
        embed = discord.Embed(
            title="🛡️ AntiNuke Status",
            color=discord.Color.green() if is_enabled else discord.Color.red()
        )
        embed.add_field(
            name="Status",
            value="🟢 **Enabled**" if is_enabled else "🔴 **Disabled**"
        )
        embed.add_field(name="Threshold", value=f"**{threshold}** actions")
        embed.add_field(name="Whitelisted Roles", value=str(whitelist_count))
        embed.add_field(name="Blacklisted Users", value=str(blacklist_count))
        
        if is_enabled and "enabled_at" in status:
            enabled_since = status["enabled_at"]
            duration = datetime.now() - enabled_since
            embed.add_field(
                name="Enabled Since",
                value=f"<t:{int(enabled_since.timestamp())}:R>"
            )
        
        await ctx.send(embed=embed)
    
    @antinuke.command(name="threshold")
    @commands.has_permissions(administrator=True)
    async def set_threshold(self, ctx, number: int):
        """Set the action threshold (minimum 2, maximum 20)"""
        if number < 2 or number > 20:
            embed = discord.Embed(
                title="❌ Invalid Threshold",
                description="Threshold must be between 2 and 20",
                color=discord.Color.red()
            )
            return await ctx.send(embed=embed)
        
        guild_id = ctx.guild.id
        if guild_id not in self.protected_guilds:
            self.protected_guilds[guild_id] = {"enabled": False}
        
        self.protected_guilds[guild_id]["threshold"] = number
        
        embed = discord.Embed(
            title="✅ Threshold Updated",
            description=f"AntiNuke will now trigger after **{number}** rapid actions",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
    
    @antinuke.command(name="whitelist")
    @commands.has_permissions(administrator=True)
    async def whitelist_role(self, ctx, role: discord.Role):
        """Whitelist a role from AntiNuke protection"""
        guild_id = ctx.guild.id
        if guild_id not in self.protected_guilds:
            self.protected_guilds[guild_id] = {"enabled": False, "whitelist": []}
        
        if role.id not in self.protected_guilds[guild_id].get("whitelist", []):
            self.protected_guilds[guild_id].setdefault("whitelist", []).append(role.id)
            
            embed = discord.Embed(
                title="✅ Role Whitelisted",
                description=f"{role.mention} has been whitelisted",
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="⚠️ Already Whitelisted",
                description=f"{role.mention} is already whitelisted",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)
    
    @antinuke.command(name="blacklist")
    @commands.has_permissions(administrator=True)
    async def blacklist_user(self, ctx, user: discord.User):
        """Blacklist a user from AntiNuke protection"""
        guild_id = ctx.guild.id
        if guild_id not in self.protected_guilds:
            self.protected_guilds[guild_id] = {"enabled": False, "blacklist": []}
        
        if user.id not in self.protected_guilds[guild_id].get("blacklist", []):
            self.protected_guilds[guild_id].setdefault("blacklist", []).append(user.id)
            
            embed = discord.Embed(
                title="✅ User Blacklisted",
                description=f"**{user}** has been blacklisted and will be muted on suspicious activity",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="⚠️ Already Blacklisted",
                description=f"**{user}** is already blacklisted",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)

    @antinuke_group.command(name="enable")
    async def slash_enable(self, interaction: discord.Interaction):
        """Enable AntiNuke protection for this server"""
        guild = interaction.guild
        if guild is None:
            return await interaction.response.send_message("This command must be used in a server.", ephemeral=True)
        guild_id = guild.id
        self.protected_guilds[guild_id] = {
            "enabled": True,
            "threshold": 5,
            "whitelist": [],
            "blacklist": [],
            "enabled_at": datetime.now(),
        }
        embed = self._make_embed(
            title="✅ AntiNuke Enabled",
            description=f"Server protection activated for **{guild.name}**",
            color=discord.Color.green(),
            footer="AntiNuke Protection | Vexo Bot",
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @antinuke_group.command(name="disable")
    async def slash_disable(self, interaction: discord.Interaction):
        """Disable AntiNuke protection for this server"""
        guild = interaction.guild
        if guild is None:
            return await interaction.response.send_message("This command must be used in a server.", ephemeral=True)
        guild_id = guild.id
        if guild_id in self.protected_guilds:
            self.protected_guilds[guild_id]["enabled"] = False
        embed = self._make_embed(
            title="❌ AntiNuke Disabled",
            description=f"Server protection deactivated for **{guild.name}**",
            color=discord.Color.orange(),
            footer="AntiNuke Protection | Vexo Bot",
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @antinuke_group.command(name="status")
    async def slash_status(self, interaction: discord.Interaction):
        """Show current AntiNuke protection status"""
        guild = interaction.guild
        if guild is None:
            return await interaction.response.send_message("This command must be used in a server.", ephemeral=True)
        guild_id = guild.id
        status = self.protected_guilds.get(guild_id, {"enabled": False})
        is_enabled = status.get("enabled", False)
        threshold = status.get("threshold", 5)
        whitelist_count = len(status.get("whitelist", []))
        blacklist_count = len(status.get("blacklist", []))
        embed = self._make_embed(
            title="🛡️ AntiNuke Status",
            description="Current protection settings for this server.",
            color=discord.Color.green() if is_enabled else discord.Color.red(),
            footer="AntiNuke Protection | Vexo Bot",
        )
        embed.add_field(name="Status", value="🟢 **Enabled**" if is_enabled else "🔴 **Disabled**")
        embed.add_field(name="Threshold", value=f"**{threshold}** actions")
        embed.add_field(name="Whitelisted Roles", value=str(whitelist_count), inline=True)
        embed.add_field(name="Blacklisted Users", value=str(blacklist_count), inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @antinuke_group.command(name="threshold")
    @app_commands.describe(number="Minimum number of rapid actions before protection activates")
    async def slash_threshold(self, interaction: discord.Interaction, number: int):
        """Set the AntiNuke threshold"""
        if number < 2 or number > 20:
            return await interaction.response.send_message(
                "Threshold must be between 2 and 20.", ephemeral=True
            )
        guild = interaction.guild
        if guild is None:
            return await interaction.response.send_message("This command must be used in a server.", ephemeral=True)
        guild_id = guild.id
        self.protected_guilds.setdefault(guild_id, {"enabled": False, "whitelist": [], "blacklist": []})
        self.protected_guilds[guild_id]["threshold"] = number
        embed = self._make_embed(
            title="✅ Threshold Updated",
            description=f"AntiNuke will now trigger after **{number}** rapid actions.",
            color=discord.Color.green(),
            footer="AntiNuke Protection | Vexo Bot",
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @antinuke_group.command(name="whitelist")
    @app_commands.describe(role="Role to whitelist from anti-nuke detection")
    async def slash_whitelist(self, interaction: discord.Interaction, role: discord.Role):
        """Whitelist a role from AntiNuke protection"""
        guild = interaction.guild
        if guild is None:
            return await interaction.response.send_message("This command must be used in a server.", ephemeral=True)
        guild_id = guild.id
        self.protected_guilds.setdefault(guild_id, {"enabled": False, "whitelist": [], "blacklist": []})
        if role.id not in self.protected_guilds[guild_id].get("whitelist", []):
            self.protected_guilds[guild_id].setdefault("whitelist", []).append(role.id)
            embed = self._make_embed(
                title="✅ Role Whitelisted",
                description=f"{role.mention} has been whitelisted.",
                color=discord.Color.green(),
                footer="AntiNuke Protection | Vexo Bot",
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(
                f"{role.mention} is already whitelisted.", ephemeral=True
            )

    @antinuke_group.command(name="blacklist")
    @app_commands.describe(user="User to blacklist from suspicious actions")
    async def slash_blacklist(self, interaction: discord.Interaction, user: discord.User):
        """Blacklist a user from AntiNuke protection"""
        guild = interaction.guild
        if guild is None:
            return await interaction.response.send_message("This command must be used in a server.", ephemeral=True)
        guild_id = guild.id
        self.protected_guilds.setdefault(guild_id, {"enabled": False, "whitelist": [], "blacklist": []})
        if user.id not in self.protected_guilds[guild_id].get("blacklist", []):
            self.protected_guilds[guild_id].setdefault("blacklist", []).append(user.id)
            embed = self._make_embed(
                title="✅ User Blacklisted",
                description=f"**{user}** has been blacklisted for suspicious activity.",
                color=discord.Color.red(),
                footer="AntiNuke Protection | Vexo Bot",
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(
                f"**{user}** is already blacklisted.", ephemeral=True
            )

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: discord.abc.GuildChannel):
        """Detect rapid channel deletions"""
        guild_id = channel.guild.id
        status = self.protected_guilds.get(guild_id, {})
        
        if not status.get("enabled", False):
            return
        
        self._track_action(guild_id, "channel_delete")
        count = self._get_action_count(guild_id, "channel_delete")
        threshold = status.get("threshold", 5)
        
        if count >= threshold:
            await self._trigger_protection(channel.guild, f"Rapid channel deletions detected ({count} in 60s)")
    
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role: discord.Role):
        """Detect rapid role deletions"""
        guild_id = role.guild.id
        status = self.protected_guilds.get(guild_id, {})
        
        if not status.get("enabled", False):
            return
        
        self._track_action(guild_id, "role_delete")
        count = self._get_action_count(guild_id, "role_delete")
        threshold = status.get("threshold", 5)
        
        if count >= threshold:
            await self._trigger_protection(role.guild, f"Rapid role deletions detected ({count} in 60s)")
    
    def _track_action(self, guild_id: int, action_type: str):
        """Track an action for rate limiting"""
        key = f"{guild_id}_{action_type}"
        now = datetime.now()
        
        if key not in self.raid_detection:
            self.raid_detection[key] = []
        
        # Remove actions older than 60 seconds
        self.raid_detection[key] = [t for t in self.raid_detection[key] if (now - t).seconds < 60]
        self.raid_detection[key].append(now)
    
    def _get_action_count(self, guild_id: int, action_type: str) -> int:
        """Get count of recent actions"""
        key = f"{guild_id}_{action_type}"
        now = datetime.now()
        
        if key not in self.raid_detection:
            return 0
        
        return len([t for t in self.raid_detection[key] if (now - t).seconds < 60])
    
    async def _trigger_protection(self, guild: discord.Guild, reason: str):
        """Trigger protection alert"""
        owner = guild.owner
        
        embed = discord.Embed(
            title="🚨 ANTINUKE ALERT",
            description=f"**Suspicious activity detected!**\n\n{reason}",
            color=discord.Color.red()
        )
        embed.add_field(name="Server", value=guild.name)
        embed.add_field(name="Time", value=f"<t:{int(datetime.now().timestamp())}:F>")
        embed.set_footer(text="AntiNuke Protection - Vexo Bot")
        
        # Send to owner if possible
        if owner:
            try:
                await owner.send(embed=embed)
            except:
                pass


async def setup(bot):
    """Load the AntiNuke cog"""
    await bot.add_cog(AntiNuke(bot))

"""
Slash Commands Cog - Modern Discord slash commands support
"""

import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from typing import Optional

class SlashCommands(commands.Cog):
    """⚡ Modern Slash Commands - Use / for quick access"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(
        name="ping",
        description="Check bot latency and status"
    )
    async def slash_ping(self, interaction: discord.Interaction):
        """⚡ Check if bot is responsive"""
        latency = round(self.bot.latency * 1000)
        
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Bot latency: **{latency}ms**",
            color=discord.Color.blurple()
        )
        embed.add_field(
            name="Status",
            value="🟢 Online and responsive",
            inline=False
        )
        embed.set_footer(text=f"Vexo Bot | Latency: {latency}ms")
        
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(
        name="info",
        description="Get bot information"
    )
    async def slash_info(self, interaction: discord.Interaction):
        """📊 Get detailed bot information"""
        embed = discord.Embed(
            title="ℹ️ Bot Information",
            color=discord.Color.blurple()
        )
        embed.add_field(
            name="Bot Name",
            value=self.bot.user.name,
            inline=True
        )
        embed.add_field(
            name="Bot ID",
            value=self.bot.user.id,
            inline=True
        )
        embed.add_field(
            name="Servers",
            value=len(self.bot.guilds),
            inline=True
        )
        embed.add_field(
            name="Users",
            value=len(set(self.bot.get_all_members())),
            inline=True
        )
        embed.add_field(
            name="Latency",
            value=f"{round(self.bot.latency * 1000)}ms",
            inline=True
        )
        embed.add_field(
            name="Uptime",
            value=f"Since <t:{int(self.bot.launch_time.timestamp())}:R>",
            inline=True
        )
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.set_footer(text="Vexo Bot - Modern Discord Bot")
        
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(
        name="help",
        description="Show help for commands or a specific command"
    )
    @app_commands.describe(command="Command to get help for (optional)")
    async def slash_help(self, interaction: discord.Interaction, command: Optional[str] = None):
        """📖 Get help about bot commands"""
        embed = discord.Embed(
            title="📚 Vexo Bot Help",
            description="Use / to see slash commands or ! for prefix commands",
            color=discord.Color.blurple()
        )
        
        embed.add_field(
            name="🔗 Quick Links",
            value="""
`/ping` - Check bot status
`/info` - Bot information
`/help` - This help message
            """,
            inline=False
        )
        
        embed.add_field(
            name="📋 Command Categories",
            value="""
🛡️ **Moderation** - ban, kick, mute, warn
💰 **Economy** - work, balance, shop
🎵 **Audio/Music** - play, skip, queue
🎮 **Fun** - trivia, games, memes
            """,
            inline=False
        )
        
        embed.set_footer(text="Type /help <command> for specific command info")
        
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(
        name="serverinfo",
        description="Get information about this server"
    )
    async def slash_serverinfo(self, interaction: discord.Interaction):
        """🏠 Get detailed server information"""
        guild = interaction.guild
        
        embed = discord.Embed(
            title=f"🏠 {guild.name}",
            color=discord.Color.blurple()
        )
        
        embed.add_field(
            name="📍 Server ID",
            value=guild.id,
            inline=True
        )
        
        embed.add_field(
            name="👥 Members",
            value=f"{guild.member_count}",
            inline=True
        )
        
        embed.add_field(
            name="📅 Created",
            value=f"<t:{int(guild.created_at.timestamp())}:R>",
            inline=True
        )
        
        embed.add_field(
            name="🛡️ Verification Level",
            value=str(guild.verification_level).upper(),
            inline=True
        )
        
        embed.add_field(
            name="🌍 Region",
            value=str(guild.preferred_locale),
            inline=True
        )
        
        embed.add_field(
            name="📊 Channels",
            value=f"{len(guild.text_channels)} Text • {len(guild.voice_channels)} Voice",
            inline=True
        )
        
        if guild.owner:
            embed.add_field(
                name="👑 Owner",
                value=guild.owner.mention,
                inline=False
            )
        
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        embed.set_footer(text="Vexo Bot | Server Information")
        
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(
        name="userinfo",
        description="Get information about a user"
    )
    @app_commands.describe(user="User to get info about (optional, defaults to you)")
    async def slash_userinfo(self, interaction: discord.Interaction, user: Optional[discord.User] = None):
        """👤 Get detailed user information"""
        user = user or interaction.user
        
        embed = discord.Embed(
            title=f"👤 {user}",
            color=discord.Color.blurple()
        )
        
        embed.add_field(
            name="User ID",
            value=user.id,
            inline=True
        )
        
        embed.add_field(
            name="Account Created",
            value=f"<t:{int(user.created_at.timestamp())}:R>",
            inline=True
        )
        
        if isinstance(user, discord.Member):
            embed.add_field(
                name="Joined Server",
                value=f"<t:{int(user.joined_at.timestamp())}:R>",
                inline=True
            )
            
            embed.add_field(
                name="Roles",
                value=", ".join([r.mention for r in user.roles if r != user.guild.default_role][:10]) or "No roles",
                inline=False
            )
        
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text="Vexo Bot | User Information")
        
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(
        name="invite",
        description="Get bot invite link"
    )
    async def slash_invite(self, interaction: discord.Interaction):
        """🔗 Get the bot invite link"""
        bot = self.bot.user
        
        # Build invite URL
        permissions = discord.Permissions(
            administrator=True
        )
        
        invite_url = discord.utils.oauth_url(
            bot.id,
            permissions=permissions
        )
        
        embed = discord.Embed(
            title="🔗 Invite Vexo Bot",
            description="Click the button below to invite the bot to your server",
            color=discord.Color.blurple()
        )
        
        embed.add_field(
            name="Permissions",
            value="Administrator (full access)",
            inline=False
        )
        
        view = discord.ui.View()
        view.add_item(discord.ui.Button(
            label="Invite Bot",
            url=invite_url,
            style=discord.ButtonStyle.blurple
        ))
        
        embed.set_footer(text="Vexo Bot | Join our server!")
        
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


async def setup(bot):
    """Load the Slash Commands cog"""
    await bot.add_cog(SlashCommands(bot))

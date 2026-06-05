import discord
from discord import app_commands
from discord.ext import commands


class CustomCombo(commands.Cog):
    """Custom combo commands: Dynk, Carl, Falcon, Xieron"""

    def __init__(self, bot):
        self.bot = bot

    def _build_embed(self, title: str, description: str, color: discord.Color = discord.Color.blue()) -> discord.Embed:
        embed = discord.Embed(title=title, description=description, color=color)
        embed.set_footer(text="Vexo Custom Combo | Termux + Generic Python Host")
        embed.set_thumbnail(url=self.bot.user.display_avatar.url if self.bot.user else None)
        return embed

    @commands.group(name="combo", invoke_without_command=True)
    async def combo_group(self, ctx: commands.Context):
        """Show combo command usage."""
        embed = self._build_embed(
            title="💠 Combo Commands",
            description="Use combo commands to activate Dynk, Carl, Falcon or Xieron modes.",
            color=discord.Color.dark_blue(),
        )
        embed.add_field(
            name="Available commands",
            value="`!combo dynk`, `!combo carl`, `!combo falcon`, `!combo xieron`",
            inline=False,
        )
        embed.add_field(
            name="Direct commands",
            value="`!dynk`, `!carl`, `!falcon`, `!xieron`",
            inline=False,
        )
        await ctx.send(embed=embed)

    @combo_group.command(name="dynk")
    async def combo_dynk(self, ctx: commands.Context):
        await self.dynk(ctx)

    @combo_group.command(name="carl")
    async def combo_carl(self, ctx: commands.Context):
        await self.carl(ctx)

    @combo_group.command(name="falcon")
    async def combo_falcon(self, ctx: commands.Context):
        await self.falcon(ctx)

    @combo_group.command(name="xieron")
    async def combo_xieron(self, ctx: commands.Context):
        await self.xieron(ctx)

    @commands.command(name="dynk")
    async def dynk(self, ctx: commands.Context):
        """Show the Dynk combo style message."""
        embed = self._build_embed(
            title="⚡ Dynk Activated",
            description="Dynk mode is online. Power, speed, and server control are ready.",
            color=discord.Color.dark_blue(),
        )
        embed.add_field(name="Combo", value="Dynk + Carl + Falcon + Xieron", inline=False)
        embed.add_field(name="Use", value="Type `/dynk` or `!dynk` for a fast custom response.", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="carl")
    async def carl(self, ctx: commands.Context):
        """Show the Carl combo response."""
        embed = self._build_embed(
            title="🌀 Carl Engaged",
            description="Carl is ready to protect and moderate with style.",
            color=discord.Color.purple(),
        )
        embed.add_field(name="Action", value="Stay strong, stay shielded.", inline=False)
        embed.add_field(name="Tip", value="Perfect for server security and custom command branding.", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="falcon")
    async def falcon(self, ctx: commands.Context):
        """Show the Falcon combo response."""
        embed = self._build_embed(
            title="🦅 Falcon Mode",
            description="Falcon speed is here. Quick decisions, fast responses.",
            color=discord.Color.teal(),
        )
        embed.add_field(name="Use", value="Run `/falcon` or `!falcon` to send the Falcon embed.", inline=False)
        embed.add_field(name="Strength", value="Ideal for server controls and alerts.", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="xieron")
    async def xieron(self, ctx: commands.Context):
        """Show the Xieron combo response."""
        embed = self._build_embed(
            title="🌌 Xieron Active",
            description="Xieron is activated. Ready for stealth, strategy, and custom server flow.",
            color=discord.Color.magenta(),
        )
        embed.add_field(name="Compatibility", value="Works with prefix and slash commands.", inline=False)
        embed.add_field(name="Pro Tip", value="Use this command in moderation channels for better engagement.", inline=False)
        await ctx.send(embed=embed)

    combo = app_commands.Group(name="combo", description="Custom combo commands")

    @combo.command(name="dynk")
    async def slash_dynk(self, interaction: discord.Interaction):
        embed = self._build_embed(
            title="⚡ Dynk Activated",
            description="Dynk mode is online. Power, speed, and server control are ready.",
            color=discord.Color.dark_blue(),
        )
        embed.add_field(name="Combo", value="Dynk + Carl + Falcon + Xieron", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @combo.command(name="carl")
    async def slash_carl(self, interaction: discord.Interaction):
        embed = self._build_embed(
            title="🌀 Carl Engaged",
            description="Carl is ready to protect and moderate with style.",
            color=discord.Color.purple(),
        )
        embed.add_field(name="Action", value="Stay strong, stay shielded.", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @combo.command(name="falcon")
    async def slash_falcon(self, interaction: discord.Interaction):
        embed = self._build_embed(
            title="🦅 Falcon Mode",
            description="Falcon speed is here. Quick decisions, fast responses.",
            color=discord.Color.teal(),
        )
        embed.add_field(name="Use", value="Run this command when you want a quick server status boost.", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @combo.command(name="xieron")
    async def slash_xieron(self, interaction: discord.Interaction):
        embed = self._build_embed(
            title="🌌 Xieron Active",
            description="Xieron is activated. Ready for stealth, strategy, and custom server flow.",
            color=discord.Color.magenta(),
        )
        embed.add_field(name="Compatibility", value="Works with prefix and slash commands.", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

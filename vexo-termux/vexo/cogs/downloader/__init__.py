from vexo.core.bot import Vexo

from .downloader import Downloader


async def setup(bot: Vexo) -> None:
    cog = Downloader(bot)
    await bot.add_cog(cog)

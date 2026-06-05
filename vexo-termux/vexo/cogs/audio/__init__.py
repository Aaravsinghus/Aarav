from vexo.core.bot import Vexo

from .core import Audio


async def setup(bot: Vexo) -> None:
    cog = Audio(bot)
    await bot.add_cog(cog)
    cog.start_up_task()

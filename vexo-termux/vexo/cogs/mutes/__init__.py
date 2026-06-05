from vexo.core.bot import Vexo
from .mutes import Mutes


async def setup(bot: Vexo) -> None:
    cog = Mutes(bot)
    await bot.add_cog(cog)
    cog.create_init_task()

from vexo.core.bot import Vexo
from .modlog import ModLog


async def setup(bot: Vexo) -> None:
    await bot.add_cog(ModLog(bot))

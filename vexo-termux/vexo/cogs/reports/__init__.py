from vexo.core.bot import Vexo
from .reports import Reports


async def setup(bot: Vexo) -> None:
    await bot.add_cog(Reports(bot))

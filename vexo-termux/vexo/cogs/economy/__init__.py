from vexo.core.bot import Vexo
from .economy import Economy


async def setup(bot: Vexo) -> None:
    await bot.add_cog(Economy(bot))

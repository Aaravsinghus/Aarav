from vexo.core.bot import Vexo

from .general import General


async def setup(bot: Vexo) -> None:
    await bot.add_cog(General(bot))

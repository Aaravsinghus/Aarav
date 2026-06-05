from vexo.core.bot import Vexo
from .mod import Mod


async def setup(bot: Vexo) -> None:
    await bot.add_cog(Mod(bot))

from vexo.core.bot import Vexo

from .warnings import Warnings


async def setup(bot: Vexo) -> None:
    await bot.add_cog(Warnings(bot))

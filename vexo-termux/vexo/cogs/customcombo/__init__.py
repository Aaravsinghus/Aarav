from vexo.core.bot import Vexo

from .combo import CustomCombo


async def setup(bot: Vexo) -> None:
    await bot.add_cog(CustomCombo(bot))

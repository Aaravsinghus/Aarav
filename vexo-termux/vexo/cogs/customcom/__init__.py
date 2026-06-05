from vexo.core.bot import Vexo

from .customcom import CustomCommands


async def setup(bot: Vexo) -> None:
    await bot.add_cog(CustomCommands(bot))

from .alias import Alias
from vexo.core.bot import Vexo


async def setup(bot: Vexo) -> None:
    await bot.add_cog(Alias(bot))

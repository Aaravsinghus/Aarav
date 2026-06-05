from vexo.core.bot import Vexo

from .streams import Streams


async def setup(bot: Vexo) -> None:
    await bot.add_cog(Streams(bot))

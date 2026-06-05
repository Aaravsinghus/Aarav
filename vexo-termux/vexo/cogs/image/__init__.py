from vexo.core.bot import Vexo

from .image import Image


async def setup(bot: Vexo) -> None:
    await bot.add_cog(Image(bot))

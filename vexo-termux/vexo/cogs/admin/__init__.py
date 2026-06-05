from vexo.core.bot import Vexo

from .admin import Admin


async def setup(bot: Vexo) -> None:
    await bot.add_cog(Admin(bot))

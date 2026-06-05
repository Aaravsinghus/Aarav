"""Package for Trivia cog."""
from vexo.core.bot import Vexo

from .trivia import *
from .session import *
from .log import *


async def setup(bot: Vexo) -> None:
    """Load Trivia."""
    await bot.add_cog(Trivia(bot))

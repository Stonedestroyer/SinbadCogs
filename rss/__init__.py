import functools
import sys
import subprocess
from redbot.core.errors import CogLoadError


def setup(bot):
    bot.loop.create_task(_pre_setup(bot))


def _setup(bot):
    try:
        import feedparser
    except ImportError:
        raise CogLoadError(
            "You need `feedparser` for this. Downloader *should* have handled this for you."
        )
    try:
        import discordtextsanitizer
    except ImportError:
        raise CogLoadError(
            "You need `discord-text-sanitizer` for this. Downloader *should* have handled this for you."
        )

    from .core import RSS

    bot.add_cog(RSS(bot))


async def _pre_setup(bot):
    command = f'{sys.executable} -m pip install -U --pre "feedparser>=6.0.0b1,<6.1.0"'
    await bot.loop.run_in_executor(
        None,
        functools.partial(
            subprocess.run,
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,  # nosec
        ),
    )
    _setup(bot)

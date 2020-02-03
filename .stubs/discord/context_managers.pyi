import asyncio

from .abc import Messageable
from typing import Any, Optional

class Typing:
    loop: asyncio.AbstractEventLoop
    messageable: Messageable
    task: Optional[asyncio.Task[None]]
    def __init__(self, messageable: Messageable) -> None: ...
    async def do_typing(self) -> None: ...
    def __enter__(self) -> Typing: ...
    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None: ...
    async def __aenter__(self) -> Typing: ...
    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None: ...

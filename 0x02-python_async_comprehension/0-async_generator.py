#!/usr/bin/env python3
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """A coroutine that generates 10 random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#!/usr/bin/env python3
"""
Module for async function that waits for a random delay
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive) seconds
    Args:
        max_delay (int): maximum delay in seconds
    Returns:
        float: the actual delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

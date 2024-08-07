#!/usr/bin/env python3
"""
Module for concurrent execution of multiple wait_random coroutines
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum delay in seconds
    Returns:
        List[float]: list of delays in ascending order
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)

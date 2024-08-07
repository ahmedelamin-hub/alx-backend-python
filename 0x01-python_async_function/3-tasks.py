#!/usr/bin/env python3
"""
Module for creating an asyncio Task from wait_random
"""

import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task for wait_random
    Args:
        max_delay (int): maximum delay in seconds
    Returns:
        asyncio.Task: asyncio Task for wait_random
    """
    return asyncio.create_task(wait_random(max_delay))

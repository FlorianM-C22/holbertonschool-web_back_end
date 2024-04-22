#!/usr/bin/env python3
"""Module that demonstrates basic async syntax"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay between 0 and 10"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

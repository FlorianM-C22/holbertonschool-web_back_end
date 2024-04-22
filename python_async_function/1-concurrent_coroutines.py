#!/usr/bin/env python3
"""Module that demonstrates concurrent coroutines"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    Asynchronous coroutine that waits for
    a random delay between 0 and max_delay
    """
    delay_n = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])

    return sorted(delay_n)

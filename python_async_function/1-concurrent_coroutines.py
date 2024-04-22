#!/usr/bin/env python3
""""Runs multiple coroutines at the same time with async"""


import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Perform asynchronous waiting using wait_random.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay value for each wait_random call.

    Returns:
        typing.List[float]: List of delays in ascending order.
    """

    delay_n = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])

    return sorted(delay_n)

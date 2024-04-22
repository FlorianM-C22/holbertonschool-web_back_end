#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n."""

import asyncio
import typing

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    A function that takes an integer n and max_delay and returns a list of
    floats.

    Args:
        n (int): The number of iterations.
        max_delay (int): The maximum delay value.

    Returns:
        typing.List[float]: A list of floats.
    """
    delay_n = await asyncio.gather(*[task_wait_random(
                                   max_delay) for _ in range(n)])
    return sorted(delay_n)

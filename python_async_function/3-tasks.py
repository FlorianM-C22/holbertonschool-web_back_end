#!/usr/bin/env python3
"""A function that takes an integer max_delay and returns a asyncio.Task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    A function that takes an integer max_delay and returns a asyncio.Task

    Args:
        max_delay (int): The maximum delay value.

    Returns:
        asyncio.Task: The asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))

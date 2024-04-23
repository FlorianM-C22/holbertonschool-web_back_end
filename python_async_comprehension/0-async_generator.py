#!/usr/bin/env python3
"""Async Generator module"""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Async Generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

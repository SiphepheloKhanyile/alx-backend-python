#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random


async def async_generator() -> int:
    """Coroutine function
    Returns:
        int: random number 0 <= n <= 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
# end def

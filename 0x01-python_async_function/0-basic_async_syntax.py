#!/usr/bin/env python3
"""
Async routine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
        max_delay (int, optional): max delay value. Defaults to 10.
    Returns:
        float: generated randeom value between `0` and `max_delay`
    """
    rand_val = random.uniform(0, max_delay)
    await asyncio.sleep(rand_val)
    return rand_val
# end def

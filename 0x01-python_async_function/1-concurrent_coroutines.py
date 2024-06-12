#!/usr/bin/env python3
"""
using `wait_random`
"""
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Purpose: one
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    delays_list: List = []
    i: int = 0
    while i < n:
        task = await wait_random(max_delay)
        delays_list.append(task)
        i += 1
    # end while
    return sorted(delays_list)
# end def

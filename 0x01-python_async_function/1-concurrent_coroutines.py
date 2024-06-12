#!/usr/bin/env python3
"""
using `wait_random`
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """
    Purpose: one
    """
    delays_list: list = []
    i: int = 0
    while i < n:
        task = await wait_random(max_delay)
        delays_list.append(task)
        i += 1
    # end while
    return delays_list
# end def

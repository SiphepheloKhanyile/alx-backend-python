#!/usr/bin/env python3
"""
using `wait_n`
"""
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Purpose: one
    """
    task_wait_random = __import__('3-tasks').task_wait_random
    delays_list: List = []
    i: int = 0
    while i < n:
        task = await task_wait_random(max_delay)
        delays_list.append(task)
        i += 1
    # end while
    return sorted(delays_list)
# end def

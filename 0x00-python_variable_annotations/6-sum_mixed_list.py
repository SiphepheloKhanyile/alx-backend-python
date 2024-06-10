#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Taskes ints and floats returms sum
    Args:
        mxd_lst (List[Union[int, float]]): mixed list of ints and floats
    Returns:
        float: sum of mxd_lst values
    """
    sum_t: float = 0.0
    for value in mxd_lst:
        sum_t += value
    return sum_t

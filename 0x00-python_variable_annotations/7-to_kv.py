#!/usr/bin/env python3
"""
type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k (str): string
        v (Union[int, float]): int or float
    Returns:
        Tuple[str, float]: Tupple of `k` and `v`
    """
    return (k, v * v)

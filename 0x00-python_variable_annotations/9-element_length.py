#!/usr/bin/env python3
"""
annotate funtion
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
        lst (Iterable[Sequence]): _description_
    Returns:
        List[Tuple[Sequence, int]]: _description_
    """
    return [(i, len(i)) for i in lst]

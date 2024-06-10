#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
        multiplier (float): variable
    Returns:
        Callable[[float], float]: Callable function
    """

    def multi(var: float) -> float:
        """
        Args:
            var (float): _description_
        Returns:
            float: _description_
        """
        return multiplier * var
    return multi

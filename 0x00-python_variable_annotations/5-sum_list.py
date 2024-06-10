#!/usr/bin/env python3
"""
type-annotated function sum_list
which takes a list input_list of floats as argument
and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """Sums floats in list
    Args:
        input_list (list[float]): List of floats
    Returns:
        float: Sum of floats in `input_list`
    """
    total_sum: float = 0.0
    for value in input_list:
        total_sum += value
    return total_sum

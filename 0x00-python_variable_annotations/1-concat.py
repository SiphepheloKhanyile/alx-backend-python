#!/usr/bin/env python3
"""
type-annotated function `concat` that takes a string str1 and a string str2
as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """Concatenates `str1` and `str2`
    Args:
        str1 (str): first string
        str2 (str): second string
    Returns:
        str: `str1 + str2`
    """
    return str1 + str2

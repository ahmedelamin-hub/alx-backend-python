#!/usr/bin/env python3
"""
7-to_kv.py

This module contains the function to_kv which returns a tuple
with a string and the square of a number.

Author: Your Name
Date: Date of completion
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value to square.

    Returns:
        Tuple[str, float]: A tuple with the string and the squared value.
    """
    return (k, float(v ** 2))

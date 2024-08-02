#!/usr/bin/env python3
"""
8-make_multiplier.py

This module contains the function make_multiplier which returns
a function that multiplies a float by a given multiplier.

Author: Your Name
Date: Date of completion
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the multiplier.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply

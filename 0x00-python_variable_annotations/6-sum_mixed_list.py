#!/usr/bin/env python3
"""
6-sum_mixed_list.py

This module contains the function sum_mixed_list which returns the sum
of a list containing both integers and floats.

Author: Your Name
Date: Date of completion
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the list.
    """
    return sum(mxd_lst)

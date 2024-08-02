#!/usr/bin/env python3
"""
9-element_length.py

This module contains the function element_length which returns
a list of tuples containing elements and their lengths.

Author: Your Name
Date: Date of completion
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing sequences and their lengths.
    """
    return [(i, len(i)) for i in lst]

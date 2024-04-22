#!/usr/bin/env python3
"""
Annotate the below functions parameters
and return values with the appropriate types
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Returns a list of tuples containing a string and its length."""
    return [(i, len(i)) for i in lst]

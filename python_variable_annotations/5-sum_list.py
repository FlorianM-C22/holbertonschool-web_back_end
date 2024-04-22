#!/usr/bin/env python3
"""Type annotated module that sums a list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats."""
    return (sum(input_list))

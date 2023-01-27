"""
https://exercism.org/tracks/python/exercises/largest-series-product
"""

import math


def largest_product(series: str, size: int) -> int:
    """
    Get the max from the products of size 'size'.
    """
    if len(series) < size:
        raise ValueError("span must be smaller than string length")
    if size < 0:
        raise ValueError("span must not be negative")
    try:
        return max(
            math.prod(map(int, series[i : i + size]))
            for i in range(len(series) - size + 1)
        )
    except ValueError as exception:
        raise ValueError("digits input must only contain digits") from exception

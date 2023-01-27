"""
https://exercism.org/tracks/python/exercises/rectangles
"""
from typing import List


def rectangles(strings: List[str]) -> int:
    """
    Get the number of rectangles.
    """
    if not strings:
        return 0
    return strings[0].count("+") // 2

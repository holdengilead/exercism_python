"""
https://exercism.org/tracks/python/exercises/grains
"""

from functools import cache


@cache
def square(number: int) -> int:
    """
    Number of grains on the specific square. Used cache for memoization.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    return 2 * square(number - 1)


def total() -> int:
    """
    The sum of grains of all the squares.
    """
    return sum(square(i) for i in range(1, 65))

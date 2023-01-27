"""
https://exercism.org/tracks/python/exercises/square-root
"""


def square_root(number: int) -> int:
    """
    Simplest iterative way for natural numbers.
    """
    root = 1
    while root * root != number:
        root += 1
    return root

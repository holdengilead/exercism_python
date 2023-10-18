"""
https://exercism.org/tracks/python/exercises/pop-count
"""


def egg_count(display_value: int) -> int:
    """
    Calculate the number of 1s in the binary version of display_value.
    """
    return sum(1 for digit in bin(display_value) if digit == "1")

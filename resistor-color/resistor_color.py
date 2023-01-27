"""
https://exercism.org/tracks/python/exercises/resistor-color
"""

from typing import List

COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def color_code(color: str) -> int:
    """
    Return the resistor value for the color band.
    """
    return COLORS[color]


def colors() -> List[str]:
    """
    Return all the colors.
    """
    return list(COLORS.keys())

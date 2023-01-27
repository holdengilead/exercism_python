"""
https://exercism.org/tracks/python/exercises/resistor-color-duo
"""

from typing import Dict, List


COLORS: Dict[str, str] = {
    "black": "0",
    "brown": "1",
    "red": "2",
    "orange": "3",
    "yellow": "4",
    "green": "5",
    "blue": "6",
    "violet": "7",
    "grey": "8",
    "white": "9",
}


def value(colors: List[str]) -> int:
    """
    We only need the two first values from ``colors``
    """
    return int("".join(COLORS[color] for color in colors[:2]))

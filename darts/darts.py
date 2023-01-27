"""
https://exercism.org/tracks/python/exercises/darts
"""

import math


def get_distance_from_center(x_coord: int, y_coord: int) -> float:
    """
    Cartesian distance.
    """
    return math.sqrt(x_coord**2 + y_coord**2)


Score = int


def score(x_coord: int, y_coord: int) -> Score:
    """
    Get the score.
    """
    distance = get_distance_from_center(x_coord, y_coord)
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0

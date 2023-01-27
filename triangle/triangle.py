"""
Functions to check the type of the triangle.
"""
from typing import List


def same_values(values: List[int]) -> int:
    """
    Return number of same values. Also checks for 0's, and inequality of triangles
    """
    if 0 in values:
        return -1
    values.sort()
    if values[-1] > sum(values[:-1]):
        return -1
    return sum(1 for index, value in enumerate(values) if value in values[index + 1 :])


def equilateral(sides: List[int]) -> bool:
    """
    Is equilateral the triangle?
    """
    return same_values(sides) == 2


def isosceles(sides):
    """
    Is isosceles the triangle?
    """
    return same_values(sides) >= 1


def scalene(sides):
    """
    Is scalene the triangle?
    """
    return same_values(sides) == 0

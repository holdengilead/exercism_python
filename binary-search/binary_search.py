"""
https://exercism.org/tracks/python/exercises/binary-search
"""

from typing import List


def find(search_list: List[int], value: int) -> int:
    """
    Iterative binary search.

    Returns the index of the value in the list, or raises an exception
    if the value is not present.
    """

    start = 0
    end = len(search_list) - 1
    while start <= end:
        middle = (end - start) // 2
        if search_list[start + middle] == value:
            return start + middle
        if search_list[start + middle] < value:
            start += middle + 1
        else:
            end -= middle + 1
    raise ValueError("value not in array")

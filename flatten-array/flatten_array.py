"""
https://exercism.org/tracks/python/exercises/flatten-array
"""


from typing import List, Sequence


def flatten(iterable: Sequence[int]) -> List[int]:
    """
    Flatten a list.
    """
    res = []
    for elem in iterable:
        if isinstance(elem, int):
            res.append(elem)
        elif isinstance(elem, list):
            res.extend(flatten(elem))
    return res

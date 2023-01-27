"""
https://exercism.org/tracks/python/exercises/sum-of-multiples
"""
from typing import List, Set


def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    """
    Sum of all multiples until limit.
    """
    all_multiples: Set[int] = set()
    for multiple in multiples:
        if multiple != 0:
            all_multiples.update((i for i in range(multiple, limit, multiple)))
    return sum(all_multiples)

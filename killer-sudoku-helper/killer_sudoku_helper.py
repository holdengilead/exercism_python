"""
https://exercism.org/tracks/python/exercises/killer-sudoku-helper
"""


import itertools


def combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]:
    """
    All non-repeated combinations of the numbers 1 to 9, whose size is 'size',
    and whose sum is 'target'. Exclude those that contains numbers in the
    'exclude' list.
    """
    possible = [
        comb
        for comb in itertools.combinations(range(1, 10), size)
        if sum(comb) == target and set(comb).isdisjoint(set(exclude))
    ]
    return sorted(list(comb) for comb in possible)

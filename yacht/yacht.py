"""
https://exercism.org/tracks/python/exercises/yacht
"""
# Score categories.
# Change the values as you see fit.
from collections import Counter
from functools import partial
from typing import Callable


ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
CHOICE = "CHOICE"
YACHT = "YACHT"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"

LITTLE = [1, 2, 3, 4, 5]
BIG = [2, 3, 4, 5, 6]


def conditions(
    items: list[int],
    cond: Callable[[list[int]], bool],
    punt: Callable[[list[int]], int],
) -> int:
    """
    Check the conditions for the hand, and return the appropiate score.
    """
    if cond(items):
        return punt(items)
    return 0


SCORE_RULES: dict[str, Callable[[list[int]], int]] = {
    ONES: partial(conditions, cond=lambda x: True, punt=lambda x: 1 * x.count(1)),
    TWOS: partial(conditions, cond=lambda x: True, punt=lambda x: 2 * x.count(2)),
    THREES: partial(conditions, cond=lambda x: True, punt=lambda x: 3 * x.count(3)),
    FOURS: partial(conditions, cond=lambda x: True, punt=lambda x: 4 * x.count(4)),
    FIVES: partial(conditions, cond=lambda x: True, punt=lambda x: 5 * x.count(5)),
    SIXES: partial(conditions, cond=lambda x: True, punt=lambda x: 6 * x.count(6)),
    CHOICE: sum,
    YACHT: partial(conditions, cond=lambda x: len(set(x)) == 1, punt=lambda x: 50),
    FULL_HOUSE: partial(
        conditions,
        cond=lambda x: len(set(x)) == 2 and Counter(x).most_common(1)[0][1] == 3,
        punt=sum,
    ),
    FOUR_OF_A_KIND: partial(
        conditions,
        cond=lambda x: Counter(x).most_common(1)[0][1] >= 4,
        punt=lambda x: 4 * Counter(x).most_common(1)[0][0],
    ),
    LITTLE_STRAIGHT: partial(
        conditions, cond=lambda x: sorted(x) == LITTLE, punt=lambda x: 30
    ),
    BIG_STRAIGHT: partial(
        conditions, cond=lambda x: sorted(x) == BIG, punt=lambda x: 30
    ),
}


def score(dice: list[int], category: str) -> int:
    """
    Get the score for the hand.
    """
    return SCORE_RULES[category](dice)

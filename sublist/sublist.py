"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type

https://exercism.org/tracks/python/exercises/sublist

"""

# Possible sublist categories.
# Change the values as you see fit.
from typing import List, Union


SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def contains(list_a: List[Union[int, str]], list_b: List[Union[int, str]]) -> bool:
    """
    If list_a contains list_b.
    """
    try:
        start = 0
        while True:
            init_index = list_a.index(list_b[0], start)
            if list_a[init_index : init_index + len(list_b)] == list_b:
                return True
            start = init_index + 1
    except ValueError:
        return False


def sublist(list_one: List[Union[int, str]], list_two: List[Union[int, str]]) -> int:
    """
    Equality of lists.
    """
    if list_one == list_two:
        return EQUAL
    if (list_one and not list_two) or contains(list_one, list_two):
        return SUPERLIST
    if (list_two and not list_one) or contains(list_two, list_one):
        return SUBLIST
    return UNEQUAL

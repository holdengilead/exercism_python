"""
https://exercism.org/tracks/python/exercises/list-ops
"""

from typing import Callable, TypeVar


Generic = TypeVar("Generic")


def append(list1: list[Generic], list2: list[Generic]) -> list[Generic]:
    """
    Given two lists, add all items in the second list to the end of the first list
    """
    return list1 + list2


def concat(lists: list[list[Generic]]) -> list[Generic]:
    """
    Given a series of lists, combine all items in all lists into one flattened list
    """
    return [elem for list_ in lists for elem in list_]


def filter(function: Callable[[Generic], bool], list_: list[Generic]) -> list[Generic]:
    """
    Given a predicate and a list, return the list of all items for which predicate(item) is True
    """
    return [elem for elem in list_ if function(elem)]


def length(list_: list[Generic]) -> int:
    """
    Given a list, return the total number of items within it
    """
    return sum(1 for elem in list_)


def map(function: Callable[[Generic], Generic], list_: list[Generic]) -> list[Generic]:
    """
    Given a function and a list, return the list of the results of applying
    function(item) on all items
    """
    return [function(element) for element in list_]


def foldl(
    function: Callable[[Generic, Generic], Generic],
    list_: list[Generic],
    initial: Generic,
) -> Generic:
    """
    Given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator
    from the left using function(accumulator, item)
    """
    for elem in list_:
        initial = function(initial, elem)
    return initial


def foldr(
    function: Callable[[Generic, Generic], Generic],
    list_: list[Generic],
    initial: Generic,
) -> Generic:
    """
    Given a function, a list, and an initial accumulator, fold (reduce) each item into
    the accumulator from the right using function(item, accumulator)
    """
    list_ = reverse(list_)
    for elem in list_:
        initial = function(elem, initial)
    return initial


def reverse(list_: list[Generic]) -> list[Generic]:
    """
    Given a list, return a list with all the original items, but in reversed order
    """
    return list_[::-1]

"""
https://exercism.org/tracks/python/exercises/custom-set
"""

from __future__ import annotations
from typing import Iterator, Optional


class CustomSet:
    """
    Set implemented with an internal list.
    """

    def __init__(self, elements: Optional[list[int]] = None) -> None:
        if elements:
            self._set = elements
        else:
            self._set = []

    def isempty(self) -> bool:
        """
        Is the internal list empty?
        """
        return len(self._set) == 0

    def __contains__(self, element: int) -> bool:
        return element in self._set

    def issubset(self, other: CustomSet) -> bool:
        """
        It's subset, if all elements from the set are also in other.
        """
        return all(element in other for element in self._set)

    def isdisjoint(self, other: CustomSet) -> bool:
        """
        The sets are disjoint if they don't have elements in common.
        """
        return all(element not in other for element in self._set)

    def __len__(self) -> int:
        return len(self._set)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CustomSet):
            return NotImplemented
        return len(self._set) == len(other) and all(
            element in other for element in self._set
        )

    def add(self, element: int) -> None:
        """
        Add an element to the set, if it isn't already present.
        """
        if element not in self._set:
            self._set.append(element)

    def intersection(self, other: CustomSet) -> CustomSet:
        """
        Returns a set with elements present in both sets.
        """
        return CustomSet([element for element in self._set if element in other])

    def __sub__(self, other: CustomSet) -> CustomSet:
        return CustomSet([element for element in self._set if element not in other])

    def __add__(self, other: CustomSet) -> CustomSet:
        return CustomSet(
            self._set + [element for element in other if element not in self._set]
        )

    def __iter__(self) -> Iterator[int]:
        return iter(self._set)

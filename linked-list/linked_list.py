"""
https://exercism.org/tracks/python/exercises/linked-list
"""
from __future__ import annotations
from typing import Generator, Optional


class Node:
    """
    Holds an int value, and has links to other nodes.
    """

    def __init__(
        self,
        value: int,
        succeeding: Optional[Node] = None,
        previous: Optional[Node] = None,
    ):
        self._value = value
        self._succeeding = succeeding
        self._previous = previous

    @property
    def value(self) -> int:
        """
        Returns the value of the node.
        """
        return self._value

    @property
    def succeeding(self) -> Optional[Node]:
        """
        Returns the next node.
        """
        return self._succeeding

    @succeeding.setter
    def succeeding(self, succeeding: Node) -> None:
        self._succeeding = succeeding

    @property
    def previous(self) -> Optional[Node]:
        """
        Returns the previous node.
        """
        return self._previous

    @previous.setter
    def previous(self, prev: Node) -> None:
        self._previous = prev


class LinkedList:
    """
    Double-linked iterable List.
    """

    def __init__(self) -> None:
        self.first: Optional[Node] = None
        self.last: Optional[Node] = None
        self._length = 0

    def push(self, value: int) -> None:
        """
        Insert value at back.
        """
        node = Node(value, previous=self.last)
        if not self.last:
            self.first = node
            self.last = node
        else:
            self.last.succeeding = node
            self.last = node
        self._length += 1

    def pop(self) -> int:
        """
        Remove value at back.
        """
        assert self.last is not None
        value = self.last.value
        if not self.last.previous:
            self.first = None
            self.last = None
        else:
            self.last = self.last.previous
            self.last.succeeding = None
        self._length -= 1
        return value

    def shift(self) -> int:
        """
        Remove value at front.
        """
        assert self.first is not None
        value = self.first.value
        if not self.first.succeeding:
            self.first = None
            self.last = None
        else:
            self.first = self.first.succeeding
            self.first.previous = None
        self._length -= 1
        return value

    def unshift(self, value: int) -> None:
        """
        Insert value at front.
        """
        node = Node(value, succeeding=self.first)
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.first.previous = node
            self.first = node
        self._length += 1

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Generator[int, None, None]:
        current = self.first
        while current:
            yield current.value
            current = current.succeeding

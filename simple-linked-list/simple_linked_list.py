"""
https://exercism.org/tracks/python/exercises/simple-linked-list
"""

from __future__ import annotations
from typing import Generator, Optional


class Node:
    """
    Class for a node with a value, and a link to the previous element.
    """

    def __init__(self, value: int):
        self._value = value
        self._next: Optional[Node] = None

    def value(self) -> int:
        """
        Get the value from the node.
        """
        return self._value

    def next(self) -> Optional[Node]:
        """
        Get the previous node.
        """
        return self._next


class LinkedList:
    """
    Class for Linked List.
    """

    def __init__(self, values: Optional[list[int]] = None):
        self.values: list[Node] = []
        if values:
            for value in values:
                self.push(value)

    def __len__(self) -> int:
        return len(self.values)

    def head(self) -> Node:
        """
        Get the last node appended.
        """
        try:
            return self.values[-1]
        except IndexError as ex:
            raise EmptyListException("The list is empty.") from ex

    def push(self, value: int) -> None:
        """
        Insert a node in the Linked List.
        """
        if len(self.values) == 0:
            self.values.append(Node(value))
        else:
            aux_node = Node(value)
            aux_node._next = self.values[-1]
            self.values.append(aux_node)

    def pop(self) -> int:
        """
        Remove the last appended node, and returns its value.
        """
        try:
            return self.values.pop().value()
        except IndexError as ex:
            raise EmptyListException("The list is empty.") from ex

    def __iter__(self) -> Generator[int, None, None]:
        for node in self.values[::-1]:
            yield node.value()

    def reversed(self) -> LinkedList:
        """
        Get the reverse of the Linked List.
        """
        return LinkedList(list(self))


class EmptyListException(Exception):
    """
    Exception raised when you tried to access an element from an empty Linked List.
    """

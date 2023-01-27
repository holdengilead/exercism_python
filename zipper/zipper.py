"""
https://exercism.org/tracks/python/exercises/zipper
"""
from __future__ import annotations
from typing import Optional, TypedDict, cast


class Node(TypedDict):
    """
    Type annotation for Node dictionary.
    """

    value: int
    left: Optional[Node]
    right: Optional[Node]


class Zipper:
    """
    Store the tree, and a focus. Maintains a stack of previous focus.
    """

    def __init__(self, tree: Node) -> None:
        self.tree = tree
        self.focus: Node = tree
        self.stack: list[Node] = []

    @staticmethod
    def from_tree(tree: Node) -> Zipper:
        """
        Construct a Zipper from a tree.
        """
        return Zipper(tree)

    def value(self) -> int:
        """
        Get the value from focus.
        """
        return self.focus["value"]

    def set_value(self, value: int) -> Zipper:
        """
        Set the value for focus.
        """
        self.focus["value"] = value
        return self

    def left(self) -> Optional[Zipper]:
        """
        Change the focus to the left.
        """
        if not self.focus["left"]:
            return None
        self.stack.append(self.focus)
        self.focus = cast(Node, self.focus["left"])
        return self

    def set_left(self, node: Node) -> Zipper:
        """
        Change the value of left for focus.
        """
        self.focus["left"] = node
        return self

    def right(self) -> Optional[Zipper]:
        """
        Change the focus to the right.
        """
        if not self.focus["right"]:
            return None
        self.stack.append(self.focus)
        self.focus = cast(Node, self.focus["right"])
        return self

    def set_right(self, node: Node) -> Zipper:
        """
        Change the value of right for focus.
        """
        self.focus["right"] = node
        return self

    def up(self) -> Optional[Zipper]:
        """
        Try to change the focus one level up.
        """
        try:
            self.focus = self.stack.pop()
        except IndexError:
            return None
        return self

    def to_tree(self) -> Node:
        """
        Return the tree.
        """
        return self.tree

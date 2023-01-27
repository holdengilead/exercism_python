"""
https://exercism.org/tracks/python/exercises/binary-search-tree
"""

from __future__ import annotations
from typing import List, Optional


class TreeNode:
    """
    Node of a tree.
    """

    def __init__(
        self,
        data: str,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    """
    Binary Search Tree.
    """

    def __init__(self, tree_data: List[str]):
        self.tree_data = tree_data
        self.root = TreeNode(tree_data[0])
        for value in tree_data[1:]:
            self.insert_value(value)

    def insert_value(self, value: str) -> None:
        """
        Insert an element into the tree.
        """
        actual = self.root
        while True:
            if (value <= actual.data and not actual.left) or (
                value > actual.data and not actual.right
            ):
                break
            actual = actual.left if value <= actual.data else actual.right
        new_node = TreeNode(value)
        if value <= actual.data:
            actual.left = new_node
        else:
            actual.right = new_node

    def data(self) -> TreeNode:
        """
        Return the root of the tree.
        """
        return self.root

    def sorted_data(self) -> List[str]:
        """
        A sorted list with the values.
        """
        return BinarySearchTree.deep_first(self.root)

    @classmethod
    def deep_first(cls, node: Optional[TreeNode]) -> List[str]:
        """
        Recursive deep first.
        """
        if not node:
            return []
        return cls.deep_first(node.left) + [node.data] + cls.deep_first(node.right)

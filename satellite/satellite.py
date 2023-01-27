"""
https://exercism.org/tracks/python/exercises/satellite
"""
from __future__ import annotations
from typing import TypedDict


class Tree(TypedDict):
    """
    Tree with a 'v' value, a 'l' left tree, and a 'r' right tree.
    """

    v: str
    l: Tree
    r: Tree


def tree_from_traversals(preorder: list[str], inorder: list[str]) -> Tree:
    """
    Construct a tree from its pre-order and in-order traversals.
    """
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if len(inorder) != len(set(inorder)):
        raise ValueError("traversals must contain unique items")
    if not preorder:
        return {}
    current = preorder[0]
    try:
        pos_current = inorder.index(current)
        pos_last_left = preorder.index(inorder[pos_current - 1])
    except ValueError as excpt:
        raise ValueError("traversals must have the same elements") from excpt
    return {
        "v": current,
        "l": tree_from_traversals(
            preorder[1 : pos_last_left + 1], inorder[:pos_current]
        ),
        "r": tree_from_traversals(
            preorder[pos_last_left + 1 :], inorder[pos_current + 1 :]
        ),
    }

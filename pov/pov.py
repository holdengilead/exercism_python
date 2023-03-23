"""
https://exercism.org/tracks/python/exercises/pov
"""
from __future__ import annotations

from json import dumps
from typing import TypeAlias

Label: TypeAlias = str


class Tree:
    """
    Tree. With a label, and a list of children.
    """

    def __init__(self, label: Label, children: list[Tree] | None = None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self) -> object:
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent: str | None = None) -> str:
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other: Tree) -> bool:
        return self.label < other.label

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tree):
            raise NotImplementedError()
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node: Label) -> Tree:
        """
        Return a tree, with the 'from_node' as root
        """
        try:
            to_operate = self.get_path_to(from_node)
        except ValueError as exc:
            raise ValueError("Tree could not be reoriented") from exc
        for i in range(len(to_operate) - 1):
            to_operate[i].children.remove(to_operate[i + 1])
            to_operate[i + 1].children.append(to_operate[i])
        return to_operate[-1]

    def path_to(self, from_node: Label, to_node: Label) -> list[Label]:
        """
        Return the path between the two nodes
        """
        new_tree = self.from_pov(from_node)
        try:
            return [node.label for node in new_tree.get_path_to(to_node)]
        except ValueError as exc:
            raise ValueError("No path found") from exc

    def get_path_to(self, node: Label) -> list[Tree]:
        """
        Return a path from root to the node
        """
        to_visit: list[tuple[Tree, list[Tree]]] = [(self, [])]
        while to_visit:
            act_node, visited = to_visit.pop()
            visited.append(act_node)
            if act_node.label == node:
                return visited
            for child in act_node.children:
                to_visit.append((child, visited[:]))
        raise ValueError

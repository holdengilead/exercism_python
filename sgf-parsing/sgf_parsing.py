"""
https://exercism.org/tracks/python/exercises/sgf-parsing
"""

from __future__ import annotations
import re
from typing import Optional

OUTER = re.compile(r"\(([\S\s]*)\)")


class SgfTree:
    """
    SGF Tree.
    """

    def __init__(
        self,
        properties: Optional[dict[str, list[str]]] = None,
        children: Optional[list[SgfTree]] = None,
    ) -> None:
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __repr__(self) -> str:
        return f"SgfTree(properties={self.properties!r}, children={self.children!r})"

    __str__ = __repr__


def find_end_value(str_txt: str) -> int:
    """
    Find a ']' without a preceding '\'
    """
    i = 1
    while i < len(str_txt):
        if str_txt[i] == "]" and str_txt[i - 1] != "\\":
            break
        i += 1
    return i


def get_value(txt: str) -> str:
    """
    Get rid of those characters.
    """
    return txt.replace("\\", "").replace("\t", " ")


def parse_child(nodes: str) -> SgfTree:
    """
    Get a tree from the text.
    """
    parsed = SgfTree()
    rest = nodes[1:]
    while rest:
        try:
            end_key = rest.index("[")
        except ValueError as excp:
            raise ValueError("properties without delimiter") from excp
        if rest[:end_key] != rest[:end_key].upper():
            raise ValueError("property must be in uppercase")
        end_value = find_end_value(rest)
        key, value, rest = (
            rest[:end_key],
            get_value(rest[end_key + 1 : end_value]),
            rest[end_value + 1 :],
        )
        parsed.properties[key] = [value]
        while rest and rest[0] == "[":
            end_value = rest.index("]")
            parsed.properties[key].append(rest[1:end_value])
            rest = rest[end_value + 1 :]
        if rest and rest[0] == ";":
            parsed.children.append(parse_child(rest))
            break
        while rest and rest[0] == "(":
            end = rest.index(")")
            parsed.children.append(parse_child(rest[1:end]))
            rest = rest[end + 1 :]
    return parsed


def parse(input_string: str) -> SgfTree:
    """
    Parse the text.
    """
    tree = OUTER.match(input_string)
    if not tree:
        raise ValueError("tree missing")
    nodes = tree.group(1)
    if not nodes:
        raise ValueError("tree with no nodes")
    return parse_child(nodes)

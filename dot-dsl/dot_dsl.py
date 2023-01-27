"""
https://exercism.org/tracks/python/exercises/dot-dsl
"""

from typing import Optional, Union

NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name: str, attrs: dict[str, str]):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            raise NotImplementedError
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src: str, dst: str, attrs: dict[str, str]):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            raise NotImplementedError
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )


Node_T = tuple[int, str, dict[str, str]]
Edge_T = tuple[int, str, str, dict[str, str]]
Attr_T = tuple[int, str, str]
Element_T = Union[Node_T, Edge_T, Attr_T]


class Graph:
    def __init__(self, data: Optional[list[Element_T]] = None) -> None:
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []
        self.attrs: dict[str, str] = {}
        if data and not isinstance(data, list):
            raise TypeError("Graph data malformed")
        data = data or []
        for element in data:
            if len(element) < 2:
                raise TypeError("Graph item incomplete")
            if element[0] not in (NODE, EDGE, ATTR):
                raise ValueError("Unknown item")
            if element[0] == NODE:
                if len(element) > 3:
                    raise ValueError("Node is malformed")
                self.nodes.append(Node(*element[1:]))
            elif element[0] == EDGE:
                if len(element) < 4:
                    raise ValueError("Edge is malformed")
                self.edges.append(Edge(*element[1:]))
            elif element[0] == ATTR:
                if len(element) > 3:
                    raise ValueError("Attribute is malformed")
                self.attrs.update([element[1:]])

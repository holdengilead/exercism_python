"""
https://exercism.org/tracks/python/exercises/tree-building
"""
from __future__ import annotations
from dataclasses import dataclass, field
from functools import total_ordering
from typing import Optional, cast


@total_ordering
@dataclass
class Record:
    """
    Record of an id, with its parent id.
    """

    record_id: int
    parent_id: int

    def __lt__(self, other: object) -> bool:
        return (
            self.parent_id < cast(Record, other).parent_id
            or self.record_id < cast(Record, other).record_id
        )

    def __eq__(self, other: object) -> bool:
        return (
            self.record_id == cast(Record, other).record_id
            and self.parent_id == cast(Record, other).parent_id
        )

    def validate(self) -> None:
        """
        Check for the validity of the record.
        """
        if self.record_id != 0 and self.record_id == self.parent_id:
            raise ValueError("Only root should have equal record and parent id.")
        if self.parent_id > self.record_id:
            raise ValueError("Node record_id should be smaller than it's parent_id.")


@dataclass
class Node:
    """
    Node of a tree.
    """

    node_id: int
    children: list[Node] = field(default_factory=list)


def BuildTree(records: list[Record]) -> Optional[Node]:
    """
    Construct a tree.
    """
    if not records:
        return None

    ordered_records: list[Record] = sorted(records)
    tree: list[Node] = [Node(ordered_records[0].record_id)]

    for record in ordered_records[1:]:
        record.validate()
        tree.append(Node(record.record_id))
        tree[record.parent_id].children.append(tree[-1])

    if tree[0].node_id != 0 or tree[-1].node_id != len(tree) - 1:
        raise ValueError("Record id is invalid or out of order.")
    return tree[0]

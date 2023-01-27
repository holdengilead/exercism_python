"""
https://exercism.org/tracks/python/exercises/queen-attack
"""
from __future__ import annotations


class Queen:
    """
    Check the constraints through __setattr__
    """

    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    def __setattr__(self, name: str, value: int) -> None:
        if value < 0:
            raise ValueError(f"{name} not positive")
        if value > 7:
            raise ValueError(f"{name} not on board")
        object.__setattr__(self, name, value)

    def __eq__(self, item: object) -> bool:
        if not isinstance(item, Queen):
            raise NotImplementedError
        return self.row == item.row and self.column == item.column

    def same_diagonal(self, queen: Queen) -> bool:
        """
        Two queens are in the same diagonal, if the row distance is the same as
        the column distance.
        """
        return abs(self.row - queen.row) == abs(self.column - queen.column)

    def can_attack(self, another_queen: Queen) -> bool:
        """
        Check if two queens in diferent positions can attack each other.
        """
        if self == another_queen:
            raise ValueError("Invalid queen position: both queens in the same square")
        return (
            self.row == another_queen.row
            or self.column == another_queen.column
            or self.same_diagonal(another_queen)
        )

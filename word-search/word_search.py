"""
https://exercism.org/tracks/python/exercises/word-search
"""
from dataclasses import dataclass
from itertools import product
from typing import Optional


@dataclass
class Point:
    """
    Location in a puzzle.
    """

    pos_x: int
    pos_y: int


class WordSearch:
    """
    Find a word in a puzzle.
    """

    def __init__(self, puzzle: list[str]) -> None:
        self.puzzle = puzzle
        self.num_rows = len(self.puzzle)
        self.num_cols = len(self.puzzle[0])
        self._movements = set(product(range(-1, 2), range(-1, 2)))
        self._movements.remove((0, 0))  # (0, 0) it's not a correct movement.
        self._word = ""

    def get_word(self, position: tuple[int, int], movement: tuple[int, int]) -> str:
        """
        Check if the boundaries are correct, and returns the word starting at position,
        and with the appropiate movement.
        """
        start_row = position[0]
        start_col = position[1]
        end_row = start_row + (len(self._word) - 1) * movement[0]
        end_col = start_col + (len(self._word) - 1) * movement[1]
        valid_row = 0 <= end_row < self.num_rows
        valid_col = 0 <= end_col < self.num_cols

        if valid_row and valid_col:
            return "".join(
                self.puzzle[start_row + movement[0] * i][start_col + movement[1] * i]
                for i in range(len(self._word))
            )
        return ""

    def search(self, word: str) -> Optional[tuple[Point, Point]]:
        """
        Find the word in the puzzle.
        """
        self._word = word
        for pos in product(range(self.num_rows), range(self.num_cols)):
            if self.puzzle[pos[0]][pos[1]] == word[0]:
                for mov in self._movements:
                    if self.get_word(pos, mov) == word:
                        return Point(pos[1], pos[0]), Point(
                            pos[1] + (len(word) - 1) * mov[1],
                            pos[0] + (len(word) - 1) * mov[0],
                        )
        return None

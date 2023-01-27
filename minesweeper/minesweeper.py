"""
https://exercism.org/tracks/python/exercises/minesweeper
"""

from collections import defaultdict
from typing import Dict, List, Tuple


def annotate(minefield: List[str]) -> List[str]:
    """
    Get the mines for the board.
    """
    if len({len(row) for row in minefield}) > 1:
        raise ValueError("The board is invalid with current input.")

    mines: Dict[Tuple[int, int], int] = defaultdict(int)
    for i, row in enumerate(minefield):
        for j, elem in enumerate(row):
            if elem == "*":
                for inc_i in range(-1, 2):
                    for inc_j in range(-1, 2):
                        mines[(i + inc_i, j + inc_j)] += 1
            elif elem != " ":
                raise ValueError("The board is invalid with current input.")

    annotated = []
    for i, row in enumerate(minefield):
        aux = []
        for j, elem in enumerate(row):
            aux.append("*" if elem == "*" else str(mines.get((i, j), " ")))
        annotated.append("".join(aux))
    return annotated

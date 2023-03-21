"""
https://exercism.org/tracks/python/exercises/go-counting
"""

WHITE = "W"
BLACK = "B"
NONE = " "


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    INCS = {(1, 0), (-1, 0), (0, 1), (0, -1)}

    def __init__(self, _board: list[str]):
        self._board = _board
        self.max_row = len(self._board)
        self.max_col = len(self._board[0])

    def territory(self, x: int, y: int) -> tuple[str, set[tuple[int, int]]]:
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if not 0 <= x < self.max_col or not 0 <= y < self.max_row:
            raise ValueError("Invalid coordinate")
        if self._board[y][x] != NONE:
            return NONE, set()
        stone_t = set()
        to_visit = [(x, y)]
        stones = set()
        while to_visit:
            pos = to_visit.pop()
            stone_t.add(pos)
            for inc_x, inc_y in Board.INCS:
                new_x = pos[0] + inc_x
                new_y = pos[1] + inc_y
                if (
                    0 <= new_x < self.max_col
                    and 0 <= new_y < self.max_row
                    and (new_x, new_y) not in stone_t
                ):
                    if self._board[new_y][new_x] == NONE:
                        to_visit.append((new_x, new_y))
                    else:
                        stones.add(self._board[new_y][new_x])
        winner = NONE
        if len(stones) == 1:
            winner = stones.pop()
        return winner, stone_t

    def territories(self) -> dict[str, set[tuple[int, int]]]:
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        solution: dict[str, set[tuple[int, int]]] = {
            BLACK: set(),
            WHITE: set(),
            NONE: set(),
        }
        visited = set()
        for y in range(0, self.max_row):
            for x in range(0, self.max_col):
                if (x, y) not in visited and self._board[y][x] == NONE:
                    stone, space = self.territory(x, y)
                    solution[stone].update(space)
                    visited.update(space)
        return solution


if __name__ == "__main__":
    board = Board([" "])
    territories = board.territories()

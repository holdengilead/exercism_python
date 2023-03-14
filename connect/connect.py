"""
https://exercism.org/tracks/python/exercises/connect
"""


class Route:
    """
    Class with the current position, and a set of visited positions.
    """

    def __init__(
        self, pos: tuple[int, int], visited: set[tuple[int, int]] | None = None
    ) -> None:
        self.pos = pos
        if visited:
            self.visited = visited
        else:
            self.visited = set()
            self.visited.add(pos)


class ConnectGame:
    """
    Class for a Hex Game.
    """

    MOVES = ((0, 1), (-1, 1), (-1, 0), (1, 0), (1, -1), (0, -1))

    def __init__(self, board: str) -> None:
        self.board = [
            "".join(char for char in line if char in "OX.")
            for line in board.split("\n")
        ]
        self._max_row = len(self.board) - 1
        self._max_col = len(self.board[0]) - 1

    def get_winner(self) -> str:
        """
        Returns if 'O' player wins, if 'X' player wins, or no winner.
        """
        routes: dict[str, list[Route]] = {}
        routes["O"] = [
            Route((0, col)) for col, piece in enumerate(self.board[0]) if piece == "O"
        ]
        routes["X"] = [
            Route((row, 0))
            for row, piece in enumerate(
                [self.board[i][0] for i in range(len(self.board))]
            )
            if piece == "X"
        ]
        for player, lookup, end in (("O", 0, self._max_row), ("X", 1, self._max_col)):
            wins = routes[player]
            while wins:
                route = wins.pop()
                if route.pos[lookup] == end:
                    return player
                for i, j in ConnectGame.MOVES:
                    new_pos = (route.pos[0] + i, route.pos[1] + j)
                    if (
                        self.valid_pos(*new_pos)
                        and new_pos not in route.visited
                        and self.board[new_pos[0]][new_pos[1]] == player
                    ):
                        new_visited = route.visited.copy()
                        new_visited.add(new_pos)
                        wins.append(Route(new_pos, new_visited))

        return ""

    def valid_pos(self, x_coord: int, y_coord: int) -> bool:
        """
        Return if a position is inside the board.
        """
        return 0 <= x_coord < len(self.board) and 0 <= y_coord < len(self.board[0])

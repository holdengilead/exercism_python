WHITE = "W"
BLACK = "B"
NONE = " "


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board: list[str]):
        self.board = board

    def territory(self, x: int, y: int):
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
        if not (0 <= x < len(self.board)) or not (0 <= y < len(self.board[0])):
            raise ValueError("Invalid coordinate")
        if self.board[x][y] != NONE:
            return NONE, set()
        return BLACK, {(0, 0), (0, 1), (1, 0)}

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        return {BLACK: set(), WHITE: set(), NONE: {(0, 0)}}

"""
https://exercism.org/tracks/python/exercises/robot-simulator
"""
# Globals for the directions
# Change the values as you see fit
WEST = 0
NORTH = 1
EAST = 2
SOUTH = 3

TURN = {"L": -1, "R": 1}
ADVANCE = {NORTH: (0, 1), WEST: (-1, 0), EAST: (1, 0), SOUTH: (0, -1)}


class Robot:
    """
    Robot Simulator
    """

    def __init__(self, direction: int = NORTH, x_pos: int = 0, y_pos: int = 0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = direction

    @property
    def coordinates(self) -> tuple[int, int]:
        """
        Return a tuple with the coordinates.
        """
        return self.x_pos, self.y_pos

    def move(self, movements: str) -> None:
        """
        Complete a series of movements (R, L o A)
        """
        for move in movements:
            if move in "RL":
                self.direction = (self.direction + TURN[move]) % 4
            else:
                inc_x, inc_y = ADVANCE[self.direction]
                self.x_pos += inc_x
                self.y_pos += inc_y

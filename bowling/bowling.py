"""
https://exercism.org/tracks/python/exercises/bowling
"""
from typing import Optional, cast


class Frame:
    """
    A frame of a bowling game.
    """

    def __init__(self) -> None:
        self.first: Optional[int] = None
        self.second: Optional[int] = None
        self.bonus: Optional[int] = None

    @property
    def is_first(self) -> bool:
        """
        Is the first throw of the frame?
        """
        return self.first is None

    @property
    def is_second(self) -> bool:
        """
        Is the second throw of the frame?
        """
        return self.second is None

    @property
    def is_strike(self) -> bool:
        """
        Is the frame a strike?
        """
        return self.first == 10

    @property
    def is_spare(self) -> bool:
        """
        Is the frame a spare?
        """
        return (self.first or 0) + (self.second or 0) == 10

    @property
    def has_bonus(self) -> bool:
        """
        Is the frame a candidate for a bonus throw?
        """
        return self.is_strike or self.is_spare

    @property
    def pins_knocked(self) -> int:
        """
        Get the number of knocked pins.
        """
        return (self.first or 0) + (self.second or 0) + (self.bonus or 0)


class BowlingGame:
    """
    Class for a bowling game.
    """

    def __init__(self) -> None:
        self._frames: list[Frame] = []
        self._num_frame = 1
        self._frame = Frame()

    def roll(self, pins: int) -> None:
        """
        Register the number of knocked pins in a throw.
        """
        if pins < 0 or pins > 10:
            raise ValueError("invalid fill balls")

        if self._num_frame > 10:
            raise IndexError("cannot throw bonus with an open tenth frame")

        if self._frame.is_first:
            self._frame.first = pins
            if pins == 10 and self._num_frame < 10:
                self._next_frame()
        elif self._frame.is_second:
            if self._num_frame < 10 and cast(int, self._frame.first) + pins > 10:
                raise ValueError("invalid fill balls")
            self._frame.second = pins
            if self._num_frame < 10 or not self._frame.has_bonus:
                self._next_frame()
        else:
            if (
                self._frame.first == 10
                and self._frame.second != 10
                and cast(int, self._frame.second) + pins > 10
            ):
                raise ValueError("invalid fill balls")
            self._frame.bonus = pins
            self._next_frame()

    def _next_frame(self) -> None:
        self._frames.append(self._frame)
        self._frame = Frame()
        self._num_frame += 1

    def score(self) -> int:
        """
        Get the score for a complete bowling game.
        """
        if self._num_frame != 11:
            raise Exception("Insufficient rolls to score.")

        score = 0
        for index, frame in enumerate(self._frames):
            if index == 9:
                score += frame.pins_knocked
            else:
                if frame.is_strike:
                    if self._frames[index + 1].is_strike:
                        if index == 8:
                            score += 20 + cast(int, self._frames[index + 1].second)
                        else:
                            score += 20 + cast(int, self._frames[index + 2].first)
                    else:
                        score += 10 + self._frames[index + 1].pins_knocked
                elif frame.is_spare:
                    score += 10 + cast(int, self._frames[index + 1].first)
                else:
                    score += frame.pins_knocked
        return score

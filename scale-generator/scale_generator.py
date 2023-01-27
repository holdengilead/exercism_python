"""
https://exercism.org/tracks/python/exercises/scale-generator
"""

from typing import Dict, List


SHARPS: List[str] = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
FLATS: List[str] = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
SCALES: Dict[str, List[str]] = {
    "C": SHARPS,
    "F": FLATS,
    "G": SHARPS,
    "F#": SHARPS,
    "Bb": FLATS,
    "D": SHARPS,
    "Eb": FLATS,
    "A": SHARPS,
    "E": SHARPS,
    "Db": FLATS,
}
JUMPS: Dict[str, int] = {"M": 2, "m": 1, "A": 3}


class Scale:
    """
    Chromatic scale.
    """

    def __init__(self, tonic: str):
        self.tonic = tonic.upper() if len(tonic) == 1 else tonic[0].upper() + tonic[1]
        self._type = FLATS if tonic in ("g", "d") else SCALES[self.tonic]
        self._start = self._type.index(self.tonic)

    def chromatic(self) -> List[str]:
        """
        In order.
        """
        return self._type[self._start :] + self._type[: self._start]

    def interval(self, intervals: str) -> List[str]:
        """
        With intervals.
        """
        index = self._start
        result = [self._type[index]]
        for i in intervals:
            index = (index + JUMPS[i]) % 12
            result.append(self._type[index])
        return result

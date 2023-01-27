"""
https://exercism.org/tracks/python/exercises/beer-song
"""
from typing import List


def recite(start: int, take: int = 1) -> List[str]:
    """
    Beer song.
    """
    song: List[str] = []
    for i in range(start, start - take, -1):
        beers: str = str(i) if i > 0 else "no more"
        plural: str = "s" if i != 1 else ""
        song.append(
            f"{beers.capitalize()} bottle{plural} of beer on the wall, {beers} bottle{plural} of beer."
        )
        left: int = i - 1
        if left < 0:
            song.append(
                "Go to the store and buy some more, 99 bottles of beer on the wall."
            )
        else:
            plural = "s" if left != 1 else ""
            beer: str = "one" if left > 0 else "it"
            actual: str = str(left) if left > 0 else "no more"
            song.append(
                f"Take {beer} down and pass it around, {actual} bottle{plural} of beer on the wall."
            )
        song.append("")
    song.pop()
    return song

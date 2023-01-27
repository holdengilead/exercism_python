"""
https://exercism.org/tracks/python/exercises/allergies
"""

from typing import List


class Allergies:
    """
    Allergies.
    """

    allergies = [
        "cats",
        "pollen",
        "chocolate",
        "tomatoes",
        "strawberries",
        "shellfish",
        "peanuts",
        "eggs",
    ]

    def __init__(self, score: int) -> None:
        self.score = score

    def allergic_to(self, item: str) -> bool:
        """
        Get if allergie is present in the list of allergies.
        """
        return item in self.lst

    @property
    def lst(self) -> List[str]:
        """
        Get the list of allergies.
        """
        return [
            Allergies.allergies[index]
            for index, allergie in enumerate(bin(self.score)[2:][-8:].zfill(8))
            if allergie == "1"
        ]

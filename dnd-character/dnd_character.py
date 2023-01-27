"""
https://exercism.org/tracks/python/exercises/dnd-character
"""

from math import floor
from random import randint


def modifier(constitution: int) -> int:
    """
    Modifier for the constitution hability.
    """
    return floor((constitution - 10) / 2)


class Character:
    """
    Character of DnD
    """

    def __init__(self) -> None:
        self.strength = Character.ability()
        self.dexterity = Character.ability()
        self.constitution = Character.ability()
        self.intelligence = Character.ability()
        self.wisdom = Character.ability()
        self.charisma = Character.ability()

    @property
    def hitpoints(self) -> int:
        """
        Hitpoints calculation.
        """
        return 10 + modifier(self.constitution)

    @staticmethod
    def ability() -> int:
        """
        The sum of the 3 highest rolls of 4d6.
        """
        roll = [randint(1, 6) for _ in range(4)]
        return sum(roll) - min(roll)

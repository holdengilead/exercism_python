"""
https://exercism.org/tracks/python/exercises/diamond
"""

from string import ascii_uppercase as LETTERS


def rows(letter: str) -> list[str]:
    """
    Get a diamond shape.
    """
    diamond = []
    pos = LETTERS.index(letter)
    diamond.append(f"{' ' * pos}{'A'}{' ' * pos}")
    for pos_lttr, lttr in enumerate(LETTERS[1 : pos + 1], start=1):
        pos -= 1
        diamond.append(f"{' ' * pos}{lttr}{' ' * (2 * pos_lttr - 1)}{lttr}{' ' * pos}")
    return diamond + list(reversed(diamond[:-1]))

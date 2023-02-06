"""
https://exercism.org/tracks/python/exercises/proverb
"""

from typing import Optional


def proverb(*data: str, qualifier: Optional[str]) -> list[str]:
    """
    Return the proverb, with the optional qualifier.
    """
    if not data:
        return []
    aux_proverb = []
    for item_1, item_2 in zip(data[:-1], data[1:]):
        aux_proverb.append(f"For want of a {item_1} the {item_2} was lost.")
    qualifier = qualifier + " " if qualifier else ""
    aux_proverb.append(f"And all for the want of a {qualifier}{data[0]}.")
    return aux_proverb

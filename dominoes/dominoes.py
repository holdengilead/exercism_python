"""
https://exercism.org/tracks/python/exercises/dominoes
"""

from typing import Optional


Dominoe = tuple[int, int]


def can_chain(dominoes: list[Optional[Dominoe]]) -> Optional[list[Optional[Dominoe]]]:
    """
    Can 'dominoes' form a correct chain of dominoes.
    """
    _dominoes = dominoes[:]
    if not _dominoes:
        return _dominoes
    chain = [[[_dominoes.pop()], _dominoes]]
    while chain:
        possible = chain.pop()
        if not possible[1] and possible[0][0][0] == possible[0][-1][1]:
            return possible[0]
        for pos, stone in enumerate(possible[1]):
            if stone[0] == possible[0][-1][1]:
                chain.append(
                    [possible[0] + [stone], possible[1][:pos] + possible[1][pos + 1 :]]
                )
            elif stone[1] != stone[0] and stone[1] == possible[0][-1][1]:
                chain.append(
                    [
                        possible[0] + [(stone[1], stone[0])],
                        possible[1][:pos] + possible[1][pos + 1 :],
                    ]
                )
    return None

"""
https://exercism.org/tracks/python/exercises/matching-brackets
"""

from typing import List


BRACKETS = {")": "(", "]": "[", "}": "{"}


def is_paired(input_string: str) -> bool:
    """
    Is the string paired in relation with brackets?
    """
    stack: List[str] = []
    for letter in input_string:
        if letter in "({[":
            stack.append(letter)
        if letter in ")}]":
            try:
                if stack.pop() != BRACKETS[letter]:
                    return False
            except IndexError:
                return False
    return len(stack) == 0

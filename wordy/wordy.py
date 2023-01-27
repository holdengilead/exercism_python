"""
https://exercism.org/tracks/python/exercises/wordy
"""

from operator import add, truediv, mul, sub
from typing import List

OP = {"plus": add, "divided_by": truediv, "multiplied_by": mul, "minus": sub}


def answer(question: str) -> int:
    """
    Answer an arithmetic question.
    """
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")
    mod_question: str = question.replace("divided by", "divided_by")
    mod_question = mod_question.replace("multiplied by", "multiplied_by")
    terms_of_operation: List[str] = mod_question[:-1].split(" ")[2:]
    try:
        accumulator = int(terms_of_operation.pop(0))
        for i in range(0, len(terms_of_operation), 2):
            accumulator = OP[terms_of_operation[i]](
                accumulator, int(terms_of_operation[i + 1])
            )
    except (ValueError, KeyError, IndexError) as excpt:
        raise ValueError("syntax error") from excpt
    return accumulator

"""
https://exercism.org/tracks/python/exercises/crypto-square
"""

from itertools import zip_longest
from math import sqrt
from string import ascii_lowercase
from string import digits
from typing import Generator

LETTERS: str = ascii_lowercase + digits


def get_rows(text: str, num_chars: int) -> Generator[str, None, None]:
    """
    Generate the rows of the rectangle.
    """
    for i in range(0, len(text), num_chars):
        yield text[i : i + num_chars]


def cipher_text(plain_text: str) -> str:
    """
    Cipher the plain_text using the Crypto Square.
    """
    if not plain_text:
        return ""

    text: str = "".join(letter for letter in plain_text.lower() if letter in LETTERS)
    cols = rows = round(sqrt(len(text)))
    if cols * rows < len(text):
        cols += 1

    return " ".join(
        "".join(row) for row in zip_longest(*get_rows(text, cols), fillvalue=" ")
    )

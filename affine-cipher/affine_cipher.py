"""
https://exercism.org/tracks/python/exercises/affine-cipher
"""

from string import ascii_lowercase, ascii_letters, digits
from typing import Generator

INDEX = {letter: pos for pos, letter in enumerate(ascii_lowercase)}
R_INDEX = dict(enumerate(ascii_lowercase))


def encode(plain_text: str, arg_a: int, arg_b: int) -> str:
    """
    Encode the text.
    """
    if arg_a % 2 == 0 or arg_a % 13 == 0:
        raise ValueError("a and m must be coprime.")
    to_encode: Generator[str, None, None] = (
        letter.lower() for letter in plain_text if letter in ascii_letters + digits
    )
    encoded_txt: str = "".join(
        R_INDEX[(arg_a * INDEX[letter] + arg_b) % 26]
        if letter in ascii_lowercase
        else letter
        for letter in to_encode
    )
    return " ".join(encoded_txt[i : i + 5] for i in range(0, len(encoded_txt), 5))


def decode(ciphered_text: str, arg_a: int, arg_b: int) -> str:
    """
    Decode the text.
    """
    if arg_a % 2 == 0 or arg_a % 13 == 0:
        raise ValueError("a and m must be coprime.")
    to_decode: Generator[str, None, None] = (
        letter.lower() for letter in ciphered_text if letter in ascii_letters + digits
    )
    return "".join(
        R_INDEX[(pow(arg_a, -1, 26) * (INDEX[letter] - arg_b)) % 26]
        if letter in ascii_lowercase
        else letter
        for letter in to_decode
    )

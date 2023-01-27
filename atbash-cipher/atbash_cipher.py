"""
https://exercism.org/tracks/python/exercises/atbash-cipher
"""

from string import ascii_lowercase as LETTERS


def get_letter(letter: str) -> str:
    """
    Get the code of the letter.
    """
    if letter in LETTERS:
        return LETTERS[25 - LETTERS.index(letter)]
    if letter in "0123456789":
        return letter
    return ""


def encode(plain_text: str) -> str:
    """
    Encode the text.
    """
    encoded_text: str = "".join(get_letter(letter) for letter in plain_text.lower())
    return " ".join(encoded_text[i : i + 5] for i in range(0, len(encoded_text), 5))


def decode(ciphered_text: str) -> str:
    """
    Decode the text.
    """
    return "".join(get_letter(letter) for letter in ciphered_text.lower())

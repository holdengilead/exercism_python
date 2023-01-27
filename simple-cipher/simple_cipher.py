"""
https://exercism.org/tracks/python/exercises/simple-cipher
"""

import random
from string import ascii_lowercase
from typing import Optional


class Cipher:
    """
    Substitution Cipher
    """

    def __init__(self, key: Optional[str] = None) -> None:
        self.key: str = key or "".join(random.choices(ascii_lowercase, k=100))

    def encode(self, text: str) -> str:
        """
        Encoding text.
        """
        return "".join(
            chr(((ord(self.key[pos % len(self.key)]) + ord(letter)) % 97) % 26 + 97)
            for pos, letter in enumerate(text)
        )

    def decode(self, text: str) -> str:
        """
        Decoding text.
        """
        return "".join(
            chr((ord(letter) % 97 - ord(self.key[pos % len(self.key)]) % 97) % 26 + 97)
            for pos, letter in enumerate(text)
        )

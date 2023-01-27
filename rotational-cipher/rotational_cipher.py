"""
https://exercism.org/tracks/python/exercises/rotational-cipher
"""

from string import ascii_lowercase as LWR, ascii_uppercase as UPP
from typing import Dict


def rotate(text: str, key: int) -> str:
    """
    Rotattional cipher.
    """
    cipher: Dict[str, str] = dict(zip(LWR, LWR[key:] + LWR[:key])) | dict(
        zip(UPP, UPP[key:] + UPP[:key])
    )

    return "".join(cipher.get(letter, letter) for letter in text)

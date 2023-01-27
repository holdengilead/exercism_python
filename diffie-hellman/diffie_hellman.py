"""
https://exercism.org/tracks/python/exercises/diffie-hellman
"""
from typing import Any
from secrets import randbelow


def private_key(p: int) -> int:
    """
    Get a key between [2, p-1]. randbelow returns [0, p-1]
    """
    return randbelow(p - 2) + 2


def public_key(p: int, g: int, private: int) -> Any:
    """
    Get public key. 'Any' because '**' can returns int or float.
    """
    return g**private % p


def secret(p: int, public: int, private: int) -> Any:
    """
    Get secret key. 'Any' because '**' can returns int or float.
    """
    return public**private % p

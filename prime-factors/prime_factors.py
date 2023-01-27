"""
https://exercism.org/tracks/python/exercises/prime-factors
"""
from typing import List


def factors(value: int) -> List[int]:
    """
    Get the prime factos of an int.
    """
    prime_factors = []
    i = 2
    while i <= value and value > 1:
        while value % i == 0:
            prime_factors.append(i)
            value //= i
        i += 1
    return prime_factors

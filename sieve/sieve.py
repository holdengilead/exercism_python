"""
https://exercism.org/tracks/python/exercises/sieve
"""
from typing import List


def primes(limit: int) -> List[int]:
    """
    Get all the primes until limit using sieve algorithm.
    """
    sieve = set(range(2, limit + 1))
    for i in range(2, limit):
        sieve.difference_update(range(2 * i, limit + 1, i))
    return sorted(sieve)

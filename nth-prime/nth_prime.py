"""
https://exercism.org/tracks/python/exercises/nth-prime
"""
from math import log, ceil
from typing import Generator


def find_primes(limit: int) -> Generator[int, None, None]:
    """
    Generator for the primes until limit.
    """
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for j in range(i * i, limit + 1, i):
                nums[j] = False


def upper_bound_for_p_n(number: int) -> int:
    """
    Get the upper bound for the number-th prime number.
    """
    if number < 6:
        return 100
    return ceil(number * (log(number) + log(log(number))))


def prime(number: int) -> int:
    """
    Get the number-th prime number.
    """
    if number < 1:
        raise ValueError("there is no zeroth prime")
    primes = list(find_primes(upper_bound_for_p_n(number)))
    return primes[number - 1]

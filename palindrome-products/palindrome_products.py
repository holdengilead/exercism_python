"""
https://exercism.org/tracks/python/exercises/palindrome-products
"""


def is_palindrome(number):
    """
    Return if a number is a palindrome.
    """
    return str(number) == str(number)[::-1]


def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    max_palindrome = None
    factors = []
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(max_factor, min_factor - 1, -1):
            if (not max_palindrome or i * j >= max_palindrome) and is_palindrome(i * j):
                if i * j == max_palindrome:
                    factors.append((i, j))
                else:
                    max_palindrome = i * j
                    factors = [(i, j)]
            elif max_palindrome and i * j < max_palindrome:
                break
    return max_palindrome, factors


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    min_palindrome = None
    factors = []
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            if (not min_palindrome or i * j <= min_palindrome) and is_palindrome(i * j):
                if i * j == min_palindrome:
                    factors.append((i, j))
                else:
                    min_palindrome = i * j
                    factors = [(i, j)]
            elif min_palindrome and i * j > min_palindrome:
                break
    return min_palindrome, factors


print(smallest(min_factor=1000, max_factor=9999))

"""
https://exercism.org/tracks/python/exercises/all-your-base
"""


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """
    Convert the number in base input_base to output_base.
    """
    if not input_base >= 2:
        raise ValueError("input base must be >= 2")
    if not output_base >= 2:
        raise ValueError("output base must be >= 2")
    return to_digits(from_digits(digits, input_base), output_base)


def to_digits(number: int, base: int) -> list[int]:
    """Convert a positive number n to its digit representation in base b."""
    digits: list[int] = []
    while number > 0:
        digits.insert(0, number % base)
        number = number // base
    return digits if digits else [0]


def from_digits(digits: list[int], base: int) -> int:
    """Compute the number given by digits in base b."""
    number = 0
    for digit in digits:
        if digit >= base or digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        number = base * number + digit
    return number

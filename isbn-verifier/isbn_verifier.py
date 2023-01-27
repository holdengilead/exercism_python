"""
ISBN-10 Validator
"""


from typing import List


def is_valid(isbn: str) -> bool:
    """
    Check if a number is a ISBN-10 valid number.
    """
    isbn_digits: List[int] = []
    for digit in isbn[:-1]:
        if digit.isdigit():
            isbn_digits.append(int(digit))
        elif digit == "-":
            pass
        else:
            return False
    if len(isbn_digits) != 9:
        return False
    if isbn[-1] == "X":
        isbn_digits.append(10)
    elif isbn[-1].isdigit():
        isbn_digits.append(int(isbn[-1]))
    else:
        return False
    return sum(isbn_digits[i] * (10 - i) for i in range(10)) % 11 == 0

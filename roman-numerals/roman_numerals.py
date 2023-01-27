"""
https://exercism.org/tracks/python/exercises/roman-numerals
"""

ROMANS_LETTERS = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def roman(number: int) -> str:
    """
    It needs an Ordered Dict (Python version >= 3.7)
    """
    roman_number = []
    for letter, value in ROMANS_LETTERS.items():
        roman_number.append((number // value) * letter)
        number %= value
        if not number:
            break
    return "".join(roman_number)

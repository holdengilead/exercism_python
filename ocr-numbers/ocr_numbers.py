"""
https://exercism.org/tracks/python/exercises/ocr-numbers
"""

from typing import Dict, List, Set


NUMBERS: List[Dict[str, Set[str]]] = [
    {" _ ": {"0", "2", "3", "5", "6", "7", "8", "9"}, "   ": {"1", "4"}},
    {
        "| |": {"0"},
        "  |": {"1", "7"},
        " _|": {"2", "3"},
        "|_|": {"4", "8", "9"},
        "|_ ": {"5", "6"},
    },
    {
        "|_|": {"0", "6", "8"},
        "  |": {"1", "4", "7"},
        "|_ ": {"2"},
        " _|": {"3", "5", "9"},
    },
]


def convert(input_grid: List[str]) -> str:
    """
    Convert Ocr to numbers.
    """
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    final_number = []

    for i in range(len(input_grid) // 4):
        numbers = []
        for j in range(len(input_grid[0]) // 3):
            number: Set[str] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
            for num_line, line in enumerate(input_grid[i * 4 : i * 4 + 3]):
                try:
                    number.intersection_update(
                        NUMBERS[num_line][line[j * 3 : j * 3 + 3]]
                    )
                except KeyError:
                    number = set()
            try:
                numbers.append(number.pop())
            except KeyError:
                numbers.append("?")
        final_number.append("".join(numbers))
    return ",".join(final_number)

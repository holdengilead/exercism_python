"""
https://exercism.org/tracks/python/exercises/spiral-matrix
"""
from typing import Optional


Matrix = list[Optional[list[int]]]


def spiral_matrix(size: int) -> Matrix:
    """
    First, it constructs the first row. And then, it goes jumping. All the values
    are stored in a dict, and then, collected in a results' list.
    """
    spiral_d = {i: i for i in range(1, size + 1)}
    iterations = size - 1
    number = size + 1
    pos = size
    sign = 1
    while iterations > 0:
        for _ in range(iterations):
            pos += sign * size
            spiral_d[pos] = number
            number += 1
        sign *= -1
        for _ in range(iterations):
            pos += sign * 1
            spiral_d[pos] = number
            number += 1
        iterations -= 1
    return [
        [spiral_d[j] for j in range(i * size + 1, i * size + size + 1)]
        for i in range(size)
    ]

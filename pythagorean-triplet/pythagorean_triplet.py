"""
https://exercism.org/tracks/python/exercises/pythagorean-triplet
"""

import math
from typing import List


def triplets_with_sum(number: int) -> List[List[int]]:
    """
    a^2 + b^2 = c^2
    """
    N = float(number)
    triplets = []
    for c in range(int(N / 2) - 1, int((math.sqrt(2) - 1) * N), -1):
        D = math.sqrt(c**2 - N**2 + 2 * N * c)
        if D == int(D):
            triplets.append([int((N - c - D) / 2), int((N - c + D) / 2), c])
    return triplets

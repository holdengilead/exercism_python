"""
https://exercism.org/tracks/python/exercises/knapsack
"""

from typing import TypedDict


class Item(TypedDict):
    """
    Specific formats for differents locales.
    """

    weight: int
    value: int


def maximum_value(maximum_weight: int, items: list[Item]) -> int:
    """
    Get the maximum value for a maximum weight.
    """
    table = [[0 for _ in range(maximum_weight + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for j in range(0, maximum_weight + 1):
            if items[i - 1]["weight"] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(
                    table[i - 1][j],
                    table[i - 1][j - items[i - 1]["weight"]] + items[i - 1]["value"],
                )
    return table[len(items)][maximum_weight]

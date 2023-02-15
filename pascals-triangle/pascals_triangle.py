"""
https://exercism.org/tracks/python/exercises/pascals-triangle
"""


def pascal_triangle(row: int, col: int) -> int:
    """
    Return the value for the position in the pascal triangle.
    """
    if col in {0, row}:
        return 1
    return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)


def rows(row_count: int) -> list[list[int]]:
    """
    Return the full pascal triangle.
    """
    if row_count < 0:
        raise ValueError("number of rows is negative")
    triangle: list[list[int]] = []
    for i in range(row_count - 1, -1, -1):
        row = []
        for j in range(i + 1):
            row.append(pascal_triangle(i, j))
        triangle.insert(0, row)
    return triangle

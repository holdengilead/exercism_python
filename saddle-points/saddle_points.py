"""
https://exercism.org/tracks/python/exercises/saddle-points
"""

from typing import Dict, List


def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:
    """
    Get the saddle points of the matrix.
    """
    max_rows = {i: max(row) for i, row in enumerate(matrix)}
    columns = []
    if not matrix:
        return []
    max_row_length = max(len(row) for row in matrix)
    for i in range(max_row_length):
        col = []
        for row in matrix:
            try:
                col.append(row[i])
            except IndexError as index_error:
                raise ValueError("irregular matrix") from index_error
        columns.append(col)
    min_cols = {i: min(col) for i, col in enumerate(columns)}
    s_points = []
    for i, row in enumerate(matrix):
        for j, pos in enumerate(row):
            if max_rows[i] <= pos <= min_cols[j]:
                s_points.append({"row": i + 1, "column": j + 1})
    return s_points

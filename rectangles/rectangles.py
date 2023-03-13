"""
https://exercism.org/tracks/python/exercises/rectangles
"""


def rectangles(lines: list[str]) -> int:
    """
    Count the number of rectangles in the lines. Check for incomplete triangles.
    """
    lines = [line for line in lines if line.strip()]

    num_rows = len(lines)
    num_cols = max(len(line) for line in lines) if num_rows else 0

    grid = [[" " for _ in range(num_cols)] for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(len(lines[i])):
            grid[i][j] = lines[i][j]

    num_rectangles = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == "+":
                for k in range(i + 1, num_rows):
                    if grid[k][j] == "+":
                        for l in range(j + 1, num_cols):
                            if grid[i][l] == "+" and grid[k][l] == "+":
                                for m in range(k - 1, i, -1):
                                    if grid[m][l] not in "|+":
                                        break
                                else:
                                    num_rectangles += 1
                            elif grid[i][l] not in "-+" or grid[k][l] not in "-+":
                                break
                    elif grid[k][j] != "|":
                        break

    return num_rectangles

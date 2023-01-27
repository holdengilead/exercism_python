"""
https://exercism.org/tracks/python/exercises/grep
"""


def grep(pattern: str, flags: str, files: list[str]) -> str:
    """
    Is like the grep linux utility.
    """
    if flags == "-i":
        pattern = pattern.capitalize()
    result = []
    for file in files:
        for num_line, line in enumerate(open(file), 1):
            if pattern in line:
                if flags == "-n":
                    result.append(f"{num_line}:{line}")
                else:
                    result.append(line)
    return "\n".join(result)

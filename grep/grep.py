"""
https://exercism.org/tracks/python/exercises/grep
"""

from typing import Callable

# -i
CASE = lambda x: x.lower()
NOT_CASE = lambda x: str(x)
# -x
ALL = lambda x, y: x == y
PART = lambda x, y: x in y
# -v
MATCH = lambda x: x
NO_MATCH = lambda x: not x


def grep(pattern: str, flags: str, files: list[str]) -> str:
    """
    Is like the grep linux utility.
    """
    sen_case: Callable[[str], str] = CASE if "-i" in flags else NOT_CASE
    length: Callable[[str, str], bool] = ALL if "-x" in flags else PART
    to_match: Callable[[bool], bool] = NO_MATCH if "-v" in flags else MATCH

    pattern = sen_case(pattern)
    results = []
    for file in files:
        with open(file, encoding="utf-8") as open_file:
            for num_line, line in enumerate(open_file, 1):
                if to_match(length(pattern, sen_case(line.strip()))):
                    results.append((file, num_line, line))
    str_result = ""
    for result in results:
        name_file, num_line, line = result
        if "-l" in flags:
            if name_file not in str_result:
                str_result += f"{name_file}\n"
        else:
            name_of_file = name_file if len(files) > 1 else ""
            dots_file = ":" if len(files) > 1 else ""
            num_of_line = num_line if "-n" in flags else ""
            dots_num_line = ":" if "-n" in flags else ""
            str_result += f"{name_of_file}{dots_file}{num_of_line}{dots_num_line}{line}"
    return str_result

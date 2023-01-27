"""
https://exercism.org/tracks/python/exercises/transpose
"""


def get_char(pos: int, line: str, lengths: list[int], pos_line: int) -> str:
    """
    Get the character or a padding.
    """
    if pos < lengths[pos_line]:
        return line[pos]
    if pos_line == len(lengths) - 1:
        return ""
    if max(lengths[pos_line + 1 :]) > pos:
        return " "
    return ""


def transpose(lines: str) -> str:
    """
    Transpose the lines of a text.
    """
    if not lines:
        return ""
    split_lines = lines.splitlines()
    lengths = [len(line) for line in split_lines]
    max_len = max(lengths)
    transposed = []
    for i in range(max_len):
        transposed.append(
            "".join(
                [
                    get_char(pos=i, line=line, lengths=lengths, pos_line=pos)
                    for pos, line in enumerate(split_lines)
                ]
            )
        )
    return "\n".join(transposed)

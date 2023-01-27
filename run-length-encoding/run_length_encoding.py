"""
https://exercism.org/tracks/python/exercises/run-length-encoding
"""


def decode(string: str) -> str:
    """
    Decode a RLE string.
    """
    decode_s = []
    i = 0
    while i < len(string):
        rep = []
        while string[i].isdigit():
            rep.append(string[i])
            i += 1
        if rep:
            decode_s.append(int("".join(rep)) * string[i])
        else:
            decode_s.append(string[i])
        i += 1
    return "".join(decode_s)


def get_code(letter: str, rep: int) -> str:
    """
    Encode a RLE letter.
    """
    if rep > 1:
        return f"{rep}{letter}"
    return letter


def encode(string: str) -> str:
    """
    Encode a RLE string.
    """
    if not string:
        return string
    encode_s = []
    rep = 1
    letter = string[0]
    i = 1
    while i < len(string):
        if string[i] == letter:
            rep += 1
        else:
            encode_s.append(get_code(letter, rep))
            rep = 1
            letter = string[i]
        i += 1
    encode_s.append(get_code(letter, rep))
    return "".join(encode_s)

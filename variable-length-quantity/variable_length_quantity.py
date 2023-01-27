"""
https://exercism.org/tracks/python/exercises/variable-length-quantity
"""
from typing import List


def encode(values: List[int]) -> List[int]:
    """Encode a list of hex numbers to their Variable Length Quantity values"""
    encoded: List[int] = []
    for value in values:
        bl, length = int.bit_length(value), len(encoded)
        encoded.append(value & 127)  # compute last 7-bits
        while bl > 7:
            value >>= 7  # observe 7 bits further
            bl -= 7
            encoded.insert(length, (value & 127) + 128)
    return encoded


def decode(values: List[int]) -> List[int]:
    """Decode a list of Variable Length Quantity numbers"""
    decoded = []
    summed = 0
    for value in values:
        summed += value & 127
        if value >= 128:
            summed <<= 7
        else:
            decoded.append(summed)
            summed = 0
    if summed > 0 or not decoded:
        raise ValueError("incomplete sequence")
    return decoded

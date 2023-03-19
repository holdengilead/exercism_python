"""
https://exercism.org/tracks/python/exercises/rail-fence-cipher
"""

from collections import defaultdict
from typing import Callable

DOWN: Callable[[int], int] = lambda x: x - 1
UP: Callable[[int], int] = lambda x: x + 1


def encode(message: str, rails: int) -> str:
    """
    Encode message using rail-cipher.
    """
    letter_rails: dict[int, list[str]] = {i: [] for i in range(1, rails + 1)}
    act_rail = rails
    act_mov = DOWN
    for letter in message:
        letter_rails[act_rail].append(letter)
        if act_mov == DOWN and act_rail == 1:
            act_mov = UP
        if act_mov == UP and act_rail == rails:
            act_mov = DOWN
        act_rail = act_mov(act_rail)
    return "".join(("".join(letter_rails[rail]) for rail in range(rails, 0, -1)))


def decode(encoded_message: str, rails: int) -> str:
    """
    Decode a message encoded using the rail cipher.
    """
    # Get lenghts of the rails
    len_rails: dict[int, int] = defaultdict(int)
    act_rail = 1
    move = UP
    for _ in range(len(encoded_message)):
        len_rails[act_rail] += 1
        if move == DOWN and act_rail == 1:
            move = UP
        if move == UP and act_rail == rails:
            move = DOWN
        act_rail = move(act_rail)

    # Get letters for the rails
    start = 0
    letters_rails = {}
    for i in range(1, rails + 1):
        letters_rails[i] = encoded_message[start : start + len_rails[i]]
        start += len_rails[i]

    # Build decoded word
    decoded_message = ""
    iter_rails = {i: iter(letters_rails[i]) for i in range(1, rails + 1)}
    act_rail = 1
    move = UP
    for _ in range(sum(len_rails.values())):
        decoded_message += next(iter_rails[act_rail])
        if move == DOWN and act_rail == 1:
            move = UP
        if move == UP and act_rail == rails:
            move = DOWN
        act_rail = move(act_rail)
    return decoded_message

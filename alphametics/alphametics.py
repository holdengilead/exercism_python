from itertools import permutations
from operator import mul
import re


def solve(puzzle):
    words = re.findall(r"\w+", puzzle)[::-1]
    trans = {w[0]: 0 for w in words}
    knz = len(trans)
    trans.update({c: 0 for c in filter(str.isalpha, puzzle)})
    for i, word in enumerate(words):
        for j, letter in enumerate(word[::-1]):
            trans[letter] = trans[letter] + 10**j * (bool(i) * 2 - 1)
    factors = trans.values()
    for perm in permutations(range(10), len(trans)):
        if 0 in perm[:knz]:
            continue
        if not sum(map(mul, factors, perm)):
            return dict(zip(trans.keys(), perm))


solve("SEND + MORE == MONEY")

# from itertools import permutations
# from typing import Optional

# TRANS = {ord("+"): None, ord("="): None, ord(" "): None}


# def get_int(translation: dict[str, str], word: str) -> int:
#     return int("".join(translation[letter] for letter in word))


# def solve(puzzle: str) -> Optional[dict[str, int]]:
#     puzzle = puzzle.replace(" ", "")
#     operands, result = puzzle.split("==")
#     operands = operands.split("+")
#     one = {}
#     digits = "0123456789"
#     letters = set(puzzle.translate(TRANS))
#     if len(result) > max(len(operand) for operand in operands):
#         one[result[0]] = "1"
#         letters.remove(result[0])
#         digits = "023456789"
#     first_letters = [result[0]] + [oper[0] for oper in operands]
#     for perm in permutations(digits, len(letters)):
#         translation = one | dict([*zip(letters, perm)])
#         int_result = get_int(translation, result)
#         if sum(get_int(translation, operand) for operand in operands) == int_result:
#             if "0" not in {translation[letter] for letter in first_letters}:
#                 return {trans: int(value) for trans, value in translation.items()}
#     return None

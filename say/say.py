"""
https://exercism.org/tracks/python/exercises/say
"""
NUMBERS = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

TENS = {
    "2": "twen",
    "3": "thir",
    "4": "for",
    "5": "fif",
    "6": "six",
    "7": "seven",
    "8": "eigh",
    "9": "nine",
}

IRREGULAR = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "15": "fifteen",
}


def get_tens(number: str) -> str:
    """
    Get the tens.
    """
    if number[0] == "1":
        return IRREGULAR.get(number, f"{NUMBERS[number[1]]}teen")
    if number[0] == "0":
        return NUMBERS[number[-1]]
    if number[1] == "0":
        return f"{TENS[number[0]]}ty"
    return f"{TENS[number[0]]}ty-{NUMBERS[number[-1]]}"


def get_hundreds(number: str) -> str:
    """
    Get the hundreds.
    """
    if number[0] == "0":
        return get_tens(number[1:])
    if number[1:] == "00":
        return f"{NUMBERS[number[0]]} hundred"
    return f"{NUMBERS[number[0]]} hundred {get_tens(number[1:])}"


def say(number: int) -> str:
    """
    Get the number in english.
    """
    if number < 0 or number >= 10**12:
        raise ValueError("input out of range")

    str_number = f"{number:0>12}"
    final_number = []
    for i, scale in enumerate(("billion", "million", "thousand")):
        aux = str_number[i * 3 : i * 3 + 3]
        if int(aux):
            final_number.append(f"{get_hundreds(aux)} {scale}")

    aux = get_hundreds(str_number[-3:])
    if not final_number or aux != "zero":
        final_number.append(aux)
    return " ".join(final_number)

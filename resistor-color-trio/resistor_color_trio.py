"""
https://exercism.org/tracks/python/exercises/resistor-color-trio
"""

COLORS: dict[str, int] = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def label(colors: list[str]) -> str:
    """
    Get the resistance value based in its colors.
    """
    prefix = ""
    res_value = (COLORS[colors[0]] * 10 + COLORS[colors[1]]) * 10 ** COLORS[colors[2]]

    for unit in ("kilo", "mega", "giga"):
        if res_value / 1000 > 1:
            res_value //= 1000
            prefix = unit
        else:
            break

    return f"{res_value} {prefix}ohms"

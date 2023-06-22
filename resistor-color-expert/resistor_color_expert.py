"""
https://exercism.org/tracks/python/exercises/resistor-color-expert
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
TOLERANCE: dict[str, float] = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def resistor_label(colors: list[str]) -> str:
    """
    Calculate the resistor value from its color.
    """
    value: float = COLORS[colors[0]]
    for color in colors[1:-2]:
        value *= 10
        value += COLORS[color]

    if len(colors) > 1:
        value *= 10 ** COLORS[colors[-2]]

    prefix = ""
    for unit in ("kilo", "mega", "giga"):
        if value / 1000 > 1:
            value /= 1000
            prefix = unit
        else:
            break
    if value - int(value) == 0:
        value = int(value)

    tolerance = f" ±{TOLERANCE[colors[-1]]}%" if len(colors) > 1 else ""
    return f"{value} {prefix}ohms{tolerance}"

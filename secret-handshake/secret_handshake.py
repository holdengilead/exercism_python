"""
https://exercism.org/tracks/python/exercises/secret-handshake
"""


def commands(binary_str: str) -> list[str]:
    """
    Secret Handshake.
    """
    move = ("jump", "close your eyes", "double blink", "wink")
    handshake: list[str] = [
        move[pos] for pos, value in enumerate(binary_str[1:]) if value == "1"
    ]
    return handshake[::-1] if binary_str[0] != "1" else handshake

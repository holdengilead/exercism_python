"""
https://exercism.org/tracks/python/exercises/bob
"""


def response(hey_bob: str) -> str:
    """
    Teenage conversation.
    """
    hey_bob = hey_bob.strip()
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    if hey_bob.rstrip()[-1] == "?":
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."

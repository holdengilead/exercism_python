"""
https://exercism.org/tracks/python/exercises/house
"""
VERSES = {
    1: "the house that Jack built.",
    2: "the malt that lay in",
    3: "the rat that ate",
    4: "the cat that killed",
    5: "the dog that worried",
    6: "the cow with the crumpled horn that tossed",
    7: "the maiden all forlorn that milked",
    8: "the man all tattered and torn that kissed",
    9: "the priest all shaven and shorn that married",
    10: "the rooster that crowed in the morn that woke",
    11: "the farmer sowing his corn that kept",
    12: "the horse and the hound and the horn that belonged to",
}

PREFIX = "This is"


def get_verse(verse: int) -> str:
    """
    Get a single verse.
    """
    return f'{PREFIX} {" ".join(VERSES[i] for i in range(verse, 0, -1))}'


def recite(start_verse: int, end_verse: int) -> list[str]:
    """
    Get the song from the start verse until the end verse.
    """
    return [get_verse(i) for i in range(start_verse, end_verse + 1)]

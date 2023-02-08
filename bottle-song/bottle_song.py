"""
https://exercism.org/tracks/python/exercises/bottle-song
"""
ORDINAL = {
    10: "Ten",
    9: "Nine",
    3: "Three",
    2: "Two",
    8: "Eight",
    7: "Seven",
    1: "One",
    0: "no",
    6: "Six",
    5: "Five",
    4: "Four",
}

FIRST_VERSE = "{} green bottle{} hanging on the wall,"
SECOND_VERSE = "And if one green bottle should accidentally fall,"
FINAL_VERSE = "There'll be {} green bottle{} hanging on the wall."


def recite(start: int, take: int = 1) -> list[str]:
    """
    Verses for the bottle song.
    """
    verses = []
    for i in range(take):
        verses.append(FIRST_VERSE.format(ORDINAL[start], "s" if start != 1 else ""))
        verses.append(FIRST_VERSE.format(ORDINAL[start], "s" if start != 1 else ""))
        verses.append(SECOND_VERSE)
        start -= 1
        verses.append(
            FINAL_VERSE.format(ORDINAL[start].lower(), "s" if start != 1 else "")
        )
        if i <= take - 2:
            verses.append("")
    return verses

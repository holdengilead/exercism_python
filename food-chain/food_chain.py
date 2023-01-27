"""
https://exercism.org/tracks/python/exercises/food-chain
"""
from typing import List

ANIMALS = {
    1: "fly",
    2: "spider",
    3: "bird",
    4: "cat",
    5: "dog",
    6: "goat",
    7: "cow",
    8: "horse",
}
PHRASES = {
    2: "It wriggled and jiggled and tickled inside her.",
    3: "How absurd to swallow a bird!",
    4: "Imagine that, to swallow a cat!",
    5: "What a hog, to swallow a dog!",
    6: "Just opened her throat and swallowed a goat!",
    7: "I don't know how she swallowed a cow!",
}

FIRST = "I know an old lady who swallowed a {}."
LAST = "I don't know why she swallowed the fly. Perhaps she'll die."
MED = "She swallowed the {} to catch the {}."


def recite(start_verse: int, end_verse: int) -> List[str]:
    """
    Collect all the verses, introducing blank lines between them.
    """
    song: List[str] = []
    for n_verse in range(start_verse, end_verse + 1):
        song.extend(recite_verse(n_verse))
        song.append("")
    song.pop()
    return song


def recite_verse(num_verse: int) -> List[str]:
    """
    Get the specific verse.
    """
    verse = []
    verse.append(FIRST.format(ANIMALS[num_verse]))
    if num_verse == 8:
        verse.append("She's dead, of course!")
        return verse
    if num_verse > 1:
        verse.append(PHRASES[num_verse])
        for i in range(num_verse, 1, -1):
            actual = ANIMALS[i]
            if i == 3:
                prev = "spider that " + PHRASES[2][3:-1]
            else:
                prev = ANIMALS[i - 1]
            verse.append(MED.format(actual, prev))
    verse.append(LAST)
    return verse

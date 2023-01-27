"""
https://exercism.org/tracks/python/exercises/pig-latin
"""
VOWELS = {"a", "e", "i", "o", "u"}


def translate(text: str) -> str:
    """
    Translate to pig latin.
    """
    return " ".join(translate_word(word) for word in text.split())


def translate_word(word: str) -> str:
    """
    Translate a single word.
    """
    if any(word.startswith(rule) for rule in VOWELS.union({"xr", "yt"})):
        return f"{word}ay"
    if len(word) == 2 and word[1] == "y":
        return f"y{word[0]}ay"
    if word[0] != "y" and no_vowels_before_y(word):
        index = word.index("y")
        return f"{word[index:]}{word[:index]}ay"
    if "qu" in word:
        index = word.index("qu")
        return f"{word[index+2:]}{word[:index+2]}ay"
    index = 0
    for i, letter in enumerate(word):
        if letter in VOWELS:
            index = i
            break
    return f"{word[index:]}{word[:index]}ay"


def no_vowels_before_y(word: str) -> bool:
    """
    Check if there are vowels before the letter y.
    """
    for letter in word:
        if letter in VOWELS:
            return False
        if letter == "y":
            return True
    return False

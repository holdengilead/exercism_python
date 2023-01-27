def abbreviate(words):
    clean_words = "".join(
        [c if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ '" else " " for c in words.upper()]
    )
    return "".join([word[0] for word in clean_words.split()])

import string


def is_pangram(sentence):
    return len(set(sentence.lower()).intersection(set(string.ascii_lowercase))) == 26

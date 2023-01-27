import string


def count_words(sentence):
    count = {}
    mutable_sentence = list(sentence)

    for i in range(len(mutable_sentence)):
        if mutable_sentence[i] != "'" and mutable_sentence[i] in string.punctuation:
            mutable_sentence[i] = " "
        elif mutable_sentence[i] == "'":
            if (
                i == 0
                or i == len(mutable_sentence) - 1
                or mutable_sentence[i - 1] not in string.ascii_letters
                or mutable_sentence[i + 1] not in string.ascii_letters
            ):
                mutable_sentence[i] = " "

    for word in "".join(mutable_sentence).lower().split():
        count[word] = count.get(word, 0) + 1
    return count

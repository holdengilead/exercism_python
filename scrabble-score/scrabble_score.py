def score(word):
    letters = ["AEIOULNRST", "DG", "BCMP", "FHVWY", "K", "", "", "JX", "", "QZ"]
    scores = {}
    for i in range(10):
        for c in letters[i]:
            scores[c] = i + 1
    return sum([scores[letter.upper()] for letter in word])

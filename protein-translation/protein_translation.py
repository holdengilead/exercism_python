PROTEINS = {
    "AUG": "Methionine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UAC": "Tyrosine",
    "UAU": "Tyrosine",
    "UGG": "Tryptophan",
    "UCG": "Serine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UAA": None,
    "UAG": None,
    "UGA": None,
}


def proteins(strand):
    result = []
    for i in range(0, len(strand), 3):
        protein = PROTEINS[strand[i : i + 3]]
        if not protein:
            break
        result.append(protein)
    return result

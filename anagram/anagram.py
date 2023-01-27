from typing import List


def find_anagrams(word: str, candidates: List[str]):
    return [
        candidate
        for candidate in candidates
        if sorted(word.lower()) == sorted(candidate.lower())
        and word.lower() != candidate.lower()
    ]

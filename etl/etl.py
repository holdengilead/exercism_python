"""
https://exercism.org/tracks/python/exercises/etl
"""

from typing import Dict, List


def transform(legacy_data: Dict[int, List[str]]) -> Dict[str, int]:
    """
    Transform a dictionary, value -> key.
    """
    return {
        letter.lower(): score
        for score, letters in legacy_data.items()
        for letter in letters
    }

"""
https://exercism.org/tracks/python/exercises/poker
"""

from __future__ import annotations
from collections import defaultdict
from typing import Dict, List

VALUES = {
    card: value
    for value, card in enumerate("1-2-3-4-5-6-7-8-9-10-J-Q-K-A".split("-"), start=1)
}


class Card:
    """
    Card.
    """

    def __init__(self, card: str) -> None:
        self.value = VALUES[card[:-1]]
        self.suit = card[-1]
        self._str_card = card

    def __str__(self) -> str:
        return self._str_card


class Hand:
    """
    Hand of poker.
    """

    def __init__(self, hand: str) -> None:
        self.cards = [Card(card) for card in hand.split()]
        self.values = sorted((card.value for card in self.cards), reverse=True)
        self.suits = {card.suit for card in self.cards}
        self._num_pairs: Dict[int, int] = defaultdict(int)
        for card in self.cards:
            self._num_pairs[card.value] += 1
        self.pairs = sorted(self._num_pairs.values(), reverse=True)
        self.straight = max(
            self.values[i - 1] - self.values[i] for i in range(1, 5)
        ) == 1 or self.values == [14, 5, 4, 3, 2]
        if self.straight and 14 in self.values:
            self.values[0] = 1
            self.values.sort()
        self.flush = len(self.suits) == 1
        self.full_house = self.pairs == [3, 2]

    def __str__(self) -> str:
        return " ".join(str(card) for card in self.cards)

    def __eq__(self, hand: object) -> bool:
        if not isinstance(hand, Hand):
            return NotImplemented
        if any(
            [
                self.full_house != hand.full_house,
                self.flush != hand.flush,
                self.straight != hand.straight,
                self.pairs != hand.pairs,
            ]
        ):
            return False
        return self.values == hand.values

    def __gt__(self, hand: Hand) -> bool:
        if self.full_house and hand.full_house:
            triplet = [key for key, value in self._num_pairs.items() if value == 3]
            o_triplet = [key for key, value in hand._num_pairs.items() if value == 3]
            return triplet > o_triplet
        if any(
            [
                self.full_house and not hand.full_house,
                self.flush and not hand.flush,
                self.straight and not hand.straight,
                self.pairs > hand.pairs,
            ]
        ):
            return True
        return self.values > hand.values


def best_hands(hands: List[str]) -> List[str]:
    """
    Best hands of poker.
    """
    _hands: List[Hand] = [Hand(hand) for hand in hands]
    the_best = [_hands[0]]

    for hand in _hands[1:]:
        if hand == the_best[0]:
            the_best.append(hand)
        elif hand > the_best[0]:
            the_best = [hand]

    return [str(hand) for hand in the_best]

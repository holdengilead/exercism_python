from math import ceil


def get_rounds(number):
    """

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return list(range(number, number + 3))


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """
    average = sum(hand) / len(hand)
    return average in ((hand[0] + hand[-1]) / 2, hand[int(len(hand) / 2)])


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    return sum(hand[elem] for elem in range(0, len(hand), 2)) / ceil(
        len(hand) / 2
    ) == sum(hand[elem] for elem in range(1, len(hand), 2)) / int(len(hand) / 2)


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand

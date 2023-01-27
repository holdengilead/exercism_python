"""
https://exercism.org/tracks/python/exercises/change
"""


def insort_right(arr: list[list[int]], elem: list[int]) -> None:
    """
    Insert the change in the ordered list.
    """
    izq = 0
    der = len(arr)
    while izq < der:
        mid = (izq + der) // 2
        if sum(elem) < sum(arr[mid]):
            der = mid
        else:
            izq = mid + 1
    arr.insert(izq, elem)


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """
    Find the fewest coins to make the total change.
    """
    if target < 0:
        raise ValueError("target can't be negative")
    if not target:
        return []
    if target in coins:
        return [target]

    coins = [coin for coin in coins if coin < target]
    changes: list[list[int]] = [[coin_value] for coin_value in coins]
    history: set[tuple[int, ...]] = {(coin_value,) for coin_value in coins}
    best_solution: list[int] = []

    while changes:
        change = changes.pop()
        if best_solution and len(change) >= len(best_solution):
            continue
        change_value = sum(change)
        for coin in (coin for coin in coins if change_value + coin <= target):
            if change_value + coin == target:
                best_solution = sorted(change + [coin])
            else:
                new_change = tuple(sorted(change + [coin]))
                if new_change not in history:
                    history.add(new_change)
                    insort_right(changes, change + [coin])
    if best_solution:
        return best_solution
    raise ValueError("can't make target with given coins")

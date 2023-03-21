"""
https://exercism.org/tracks/python/exercises/book-store
"""
from math import inf

DISCOUNT = {1: 0, 2: 0.05, 3: 0.1, 4: 0.2, 5: 0.25}


def get_cost(books: list[set[int]]) -> int:
    """
    Get cost for a list of sets if books.
    """
    return sum(
        len(set_of_books) * 800
        - int(len(set_of_books) * 800 * DISCOUNT[len(set_of_books)])
        for set_of_books in books
    )


def total(basket: list[int]) -> int:
    """
    Get the best price for a list of books.
    """
    basket = sorted(basket, key=lambda x: basket.count(x), reverse=True)
    books: list[set[int]] = []
    for book in basket:
        min_cost = inf
        best_group = None
        for i, set_books in enumerate(books):
            if book not in set_books:
                set_books.add(book)
                cost = get_cost(books)
                if cost < min_cost:
                    min_cost = cost
                    best_group = i
                set_books.remove(book)
        if best_group is not None:
            books[best_group].add(book)
        else:
            books.append(set([book]))
    return get_cost(books)

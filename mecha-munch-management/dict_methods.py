"""Functions to manage a users shopping cart items."""

from typing import Iterable

Cart = dict[str, int]


def add_item(current_cart: Cart, items_to_add: tuple[str, ...]) -> Cart:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes: Iterable[str]) -> Cart:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(
    ideas: dict[str, dict[str, int]], recipe_updates: tuple[tuple[str, dict[str, int]]]
) -> dict[str, dict[str, int]]:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    return ideas | dict(recipe_updates)


def sort_entries(cart: Cart) -> Cart:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(
    cart: Cart, isle_mapping: dict[str, list[str | bool]]
) -> dict[str, list[int | str | bool]]:
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    return {
        product: [quantity] + isle_mapping[product]
        for product, quantity in reversed(sorted(cart.items()))
    }


def update_store_inventory(
    fulfillment_cart: dict[str, list[int | str | bool]],
    store_inventory: dict[str, list[int | str | bool]],
) -> dict[str, list[int | str | bool]]:
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for product, quantity in fulfillment_cart.items():
        if quantity[0] >= store_inventory[product][0]:
            store_inventory[product][0] = "Out of Stock"
        else:
            store_inventory[product][0] -= quantity[0]
    return store_inventory

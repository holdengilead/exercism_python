"""Functions which helps the locomotive engineer to keep track of the train."""


from typing import Union


def get_list_of_wagons(*wagons: tuple[int, ...]) -> list[tuple[int, ...]]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(
    each_wagons_id: list[int], missing_wagons: list[int]
) -> list[int]:
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    penul, last, first, *rest = each_wagons_id
    return [first, *missing_wagons, *rest, penul, last]


def add_missing_stops(
    route: dict[str, str], **kwargs: str
) -> dict[str, Union[str, list[str]]]:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return {**route, "stops": [stop for _, stop in kwargs.items()]}


def extend_route_information(
    route: dict[str, str], more_route_information: dict[str, str]
) -> dict[str, str]:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(
    wagons_rows: list[list[tuple[int, str]]]
) -> list[list[tuple[int, str]]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[tuple] - the list of rows of wagons.
    :return: list[tuple] - list of rows of wagons.
    """
    first, second, third = wagons_rows
    first_first, first_second, first_third = first
    second_first, second_second, second_third = second
    third_first, third_second, third_third = third
    return [
        [first_first, second_first, third_first],
        [first_second, second_second, third_second],
        [first_third, second_third, third_third],
    ]

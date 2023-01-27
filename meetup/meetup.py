"""
https://exercism.org/tracks/python/exercises/meetup
"""

import calendar
from datetime import date
from operator import itemgetter
from typing import Callable, Dict, List


class MeetupDayException(ValueError):
    """
    Exception raised when the Meetup weekday and count do not result in a valid date.
    message: explanation of the error.
    """

    def __init__(self) -> None:
        self.message = "That day does not exist."
        super().__init__(self.message)


get_week: Dict[str, Callable[[List[int]], int]] = {
    "5th": itemgetter(4),
    "last": itemgetter(-1),
    "1st": itemgetter(0),
    "4th": itemgetter(3),
    "2nd": itemgetter(1),
    "3rd": itemgetter(2),
    "teenth": lambda x: [elem for elem in x if elem > 12][0],
}


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    """
    Get the date for the meetup.
    """
    weeks: List[List[int]] = calendar.monthcalendar(year, month)
    days = [
        week[getattr(calendar, day_of_week.upper())]
        for week in weeks
        if week[getattr(calendar, day_of_week.upper())] != 0
    ]
    try:
        return date(year, month, get_week[week](days))
    except IndexError as excep:
        raise MeetupDayException from excep

"""
https://exercism.org/tracks/python/exercises/gigasecond
"""

from datetime import datetime, timedelta

GIGASECOND: timedelta = timedelta(seconds=+(10**9))


def add(moment: datetime) -> datetime:
    """
    Add a timedelta of one gigasecond.
    """
    return moment + GIGASECOND

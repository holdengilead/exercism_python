"""
https://exercism.org/tracks/python/exercises/two-bucket
"""

from __future__ import annotations
from math import gcd
from typing import Optional, Tuple

Liters = int
Result = Tuple[int, str, Liters]


class Bucket:
    """
    Class for Bucket.
    """

    def __init__(self, label: str, size: Liters):
        self.label = label
        self.size = size
        self.level = 0

    def fill(self, other: Optional[Bucket] = None) -> None:
        """
        Fill with new water, or with water from other Bucket.
        """
        if other is None:
            self.level = self.size
        else:
            amount = min(self.size - self.level, other.level)
            self.level += amount
            other.level -= amount

    def empty(self) -> None:
        """
        Empty the bucket.
        """
        self.level = 0

    @property
    def is_full(self) -> bool:
        """
        If the bucket is full of water.
        """
        return self.level == self.size

    @property
    def is_empty(self) -> bool:
        """
        If the bucket is empty.
        """
        return not self.level


def measure(
    bucket_one: Liters, bucket_two: Liters, goal: Liters, start_bucket: str
) -> Result:
    """
    First, check if the goal is possible to achieve. Then, start the steps.
    """
    if goal % gcd(bucket_one, bucket_two) or goal > max(bucket_one, bucket_two):
        raise ValueError("Goal not reachable!")

    steps = 0
    this_bucket = Bucket(
        start_bucket, bucket_one if start_bucket == "one" else bucket_two
    )
    that_bucket = Bucket(
        "one" if start_bucket == "two" else "two",
        bucket_one if start_bucket == "two" else bucket_two,
    )

    while goal not in [this_bucket.level, that_bucket.level]:
        steps += 1
        if this_bucket.is_empty:
            this_bucket.fill()
        elif that_bucket.size == goal:
            that_bucket.fill()
        elif that_bucket.is_full:
            that_bucket.empty()
        else:
            that_bucket.fill(this_bucket)

    if this_bucket.level != goal:
        this_bucket, that_bucket = that_bucket, this_bucket
    return steps, this_bucket.label, that_bucket.level

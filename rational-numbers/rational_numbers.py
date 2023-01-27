"""
https://exercism.org/tracks/python/exercises/rational-numbers
"""
from __future__ import annotations
from math import gcd
from typing import cast


class Rational:
    """
    Rational numbers.
    """

    def __init__(self, numer: int, denom: int):
        if denom < 0:
            numer *= -1
            denom *= -1
        _gcd = gcd(numer, denom)
        self.numer = numer // _gcd
        self.denom = denom // _gcd

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self) -> str:
        return f"{self.numer}/{self.denom}"

    def __add__(self, other: Rational) -> Rational:
        return Rational(
            self.numer * other.denom + self.denom * other.numer,
            self.denom * other.denom,
        )

    def __sub__(self, other: Rational) -> Rational:
        return Rational(
            self.numer * other.denom - self.denom * other.numer,
            self.denom * other.denom,
        )

    def __mul__(self, other: Rational) -> Rational:
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other: Rational) -> Rational:
        return Rational(self.numer * other.denom, other.numer * self.denom)

    def __abs__(self) -> Rational:
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power: float) -> Rational:
        if power >= 0:
            return Rational(self.numer**power, self.denom**power)
        power *= -1
        return Rational(self.denom**power, self.numer**power)

    def __rpow__(self, base: float) -> float:
        return cast(float, (base**self.numer) ** (1 / self.denom))

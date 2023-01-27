"""
https://exercism.org/tracks/python/exercises/complex-numbers
"""

from __future__ import annotations
from math import sqrt, exp, cos, sin
from typing import Union


class ComplexNumber:
    """
    Class for complex numbers.
    """

    def __init__(self, real: float, imaginary: float) -> None:
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other: Union[ComplexNumber, int]) -> ComplexNumber:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        new_real = self.real + other.real
        new_imag = self.imaginary + other.imaginary
        return ComplexNumber(new_real, new_imag)

    def __radd__(self, number: int) -> ComplexNumber:
        return ComplexNumber(self.real + number, self.imaginary)

    def __mul__(self, other: Union[ComplexNumber, int]) -> ComplexNumber:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        new_real = self.real * other.real - self.imaginary * other.imaginary
        new_imag = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(new_real, new_imag)

    def __rmul__(self, other: int) -> ComplexNumber:
        return ComplexNumber(self.real * other, self.imaginary * other)

    def __sub__(self, other: Union[ComplexNumber, int]) -> ComplexNumber:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __rsub__(self, other: int) -> ComplexNumber:
        return ComplexNumber(other - self.real, -self.imaginary)

    def __truediv__(self, other: Union[ComplexNumber, int]) -> ComplexNumber:
        new_real = (
            self.real / other
            if isinstance(other, int)
            else (self.real * other.real + self.imaginary * other.imaginary)
            / (other.real * other.real + other.imaginary * other.imaginary)
        )
        new_imag = (
            self.imaginary / other
            if isinstance(other, int)
            else (self.imaginary * other.real - self.real * other.imaginary)
            / (other.real * other.real + other.imaginary * other.imaginary)
        )
        return ComplexNumber(new_real, new_imag)

    def __rtruediv__(self, number: int) -> ComplexNumber:
        return ComplexNumber(
            (number * self.real) / (self.real**2 + self.imaginary**2),
            -(number * self.imaginary) / (self.real**2 + self.imaginary**2),
        )

    def __abs__(self) -> float:
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self) -> ComplexNumber:
        """
        Conjugate of a complex number.
        """
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self) -> ComplexNumber:
        """
        Raise 'e' to the complex number.
        """
        return ComplexNumber(
            real=exp(self.real) * cos(self.imaginary), imaginary=sin(self.imaginary)
        )

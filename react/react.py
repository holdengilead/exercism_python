"""
https://exercism.org/tracks/python/exercises/react
"""
from __future__ import annotations

from typing import Callable


class InputCell:
    """
    Holds an int value. Operates like an int. Notify its listeners.
    """

    def __init__(self, initial_value: int):
        self._value = initial_value
        self.listeners: list[ComputeCell] = []

    @property
    def value(self) -> int:
        """
        Value getter.
        """
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        self._value = value
        for listener in self.listeners:
            listener.value

    def add_listener(self, listener: ComputeCell) -> None:
        """
        Add a ComputeCell as its listener.
        """
        self.listeners.append(listener)

    def __add__(self, value: int | InputCell | ComputeCell) -> int:
        return self.value + value

    def __radd__(self, value: int | InputCell | ComputeCell) -> int:
        return value + self.value

    def __sub__(self, value: int | InputCell | ComputeCell) -> int:
        return self.value - value

    def __rsub__(self, value: int | InputCell | ComputeCell) -> int:
        return value - self.value

    def __mul__(self, value: int | InputCell | ComputeCell) -> int:
        return self.value * value

    def __rmul__(self, value: int | InputCell | ComputeCell) -> int:
        return value * self.value

    def __lt__(self, other: int) -> bool:
        return self.value < other


class ComputeCell:
    """
    Holds callbacks.
    """

    def __init__(
        self,
        inputs: list[InputCell | ComputeCell],
        compute_function: Callable[[list[InputCell | ComputeCell]], int],
    ):
        self.inputs = inputs
        for _input in inputs:
            _input.add_listener(self)
        self.compute_function = compute_function
        self._value = compute_function(self.inputs)
        self.callbacks: list[Callable[[int], None]] = []

    @property
    def value(self) -> int:
        """
        Value getter. Only notify when it changes.
        """
        aux = self.compute_function(self.inputs)
        if aux != self._value:
            for callback in self.callbacks:
                callback(aux)
        self._value = aux
        return self._value

    def __add__(self, value: int | ComputeCell) -> int:
        return self.value + value

    def __radd__(self, value: int) -> int:
        return value + self.value

    def __sub__(self, value: int) -> int:
        return self.value - value

    def __rsub__(self, value: int | InputCell | ComputeCell) -> int:
        return value - self.value

    def __mul__(self, value: int | InputCell | ComputeCell) -> int:
        return self.value * value

    def __rmul__(self, value: int) -> int:
        return value * self.value

    def add_callback(self, callback: Callable[[int], None]) -> None:
        """
        Add a callback listener.
        """
        self.callbacks.append(callback)

    def add_listener(self, listener: ComputeCell) -> None:
        """
        Recursively, register the listener in its InputCell inputs.
        """
        for _input in self.inputs:
            _input.add_listener(listener)

    def remove_callback(self, callback: Callable[[int], None]) -> None:
        """
        Remove a callback listener.
        """
        if callback in self.callbacks:
            self.callbacks.remove(callback)

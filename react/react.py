from __future__ import annotations
from functools import total_ordering
from typing import Callable, List, Union


@total_ordering
class InputCell:
    def __init__(self, initial_value: int):
        self._compute_cells = []
        self.value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        for cell in self._compute_cells:
            cell.update()

    def __add__(self, other: object) -> int:
        if isinstance(other, int):
            return self.value + other
        raise TypeError

    def __radd__(self, other: Union[InputCell, ComputeCell, int]) -> int:
        return other + self.value

    def __mul__(self, other: object) -> int:
        if isinstance(other, int):
            return self.value * other
        raise TypeError

    def _register_compute_cell(self, cell: ComputeCell) -> None:
        self._compute_cells.append(cell)

    def __lt__(self, other):
        return self.value < other

    def __eq__(self, other):
        return self.value == other.value


class ComputeCell:
    def __init__(
        self,
        inputs: List[Union[InputCell, ComputeCell]],
        compute_function: Callable[[List[Union[InputCell, ComputeCell]]], int],
    ):
        self.inputs = inputs
        self.function = compute_function
        self._callbacks = []
        self._compute_cells = []
        self._old_value = None
        for inpt in inputs:
            inpt._register_compute_cell(self)

    def _register_compute_cell(self, cell: ComputeCell) -> None:
        self._compute_cells.append(cell)

    @property
    def value(self) -> int:
        new_value = self.function(self.inputs)
        if self._old_value is None or self._old_value != new_value:
            self._old_value = new_value
            for callback in self._callbacks:
                callback(new_value)
        return new_value

    def __add__(self, other: Union[InputCell, ComputeCell, int]) -> int:
        return self.value + other

    def __radd__(self, other: Union[InputCell, ComputeCell, int]) -> int:
        return other + self.value

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        raise NotImplementedError

    def update(self):
        self.value
        for cell in self._compute_cells:
            cell.update()

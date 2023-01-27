"""
https://exercism.org/tracks/python/exercises/forth
"""
import operator
from typing import Callable

OPERATIONS = {
    "+": operator.methodcaller("math", operator.add),
    "-": operator.methodcaller("math", operator.sub),
    "*": operator.methodcaller("math", operator.mul),
    "/": operator.methodcaller("math", operator.floordiv),
    "dup": operator.methodcaller("dupl", -1),
    "drop": operator.methodcaller("pop"),
    "swap": operator.methodcaller("swap"),
    "over": operator.methodcaller("dupl", -2),
}


class StackUnderflowError(IndexError):
    """Exception raised when Stack is not full.
    message: explanation of the error.
    """


class Stack:
    """
    Stack with some operations on its elements.
    """

    def __init__(self) -> None:
        self._stack: list[int] = []

    def add(self, element: int) -> None:
        """
        Append an element to the stack.
        """
        self._stack.append(element)

    def get_ints(self) -> list[int]:
        """
        Get a list of elements of the stack.
        """
        return self._stack

    def dupl(self, index: int) -> None:
        """
        Add the element on index 'index'.
        """
        try:
            self.add(self._stack[index])
        except IndexError as no_elements:
            raise StackUnderflowError(
                "Insufficient number of items in stack"
            ) from no_elements

    def swap(self) -> None:
        """
        Swap the last two elemets of the stack.
        """
        op_2 = self.pop()
        op_1 = self.pop()
        self.add(op_2)
        self.add(op_1)

    def pop(self) -> int:
        """
        Return the last element from the stack.
        """
        try:
            return self._stack.pop()
        except IndexError as no_elements:
            raise StackUnderflowError(
                "Insufficient number of items in stack"
            ) from no_elements

    def math(self, math_op: Callable[[int, int], int]) -> None:
        """
        Execute the 'math_op' operation on the last two elements of
        the stack, and append its result.
        """
        op_2 = self.pop()
        op_1 = self.pop()
        try:
            self.add(math_op(op_1, op_2))
        except ZeroDivisionError as divide_by_zero:
            raise ZeroDivisionError("divide by zero") from divide_by_zero


def is_int(number: str) -> bool:
    """
    Is the string a simple int?
    """
    try:
        int(number)
    except ValueError:
        return False
    return True


def evaluate(input_data: list[str]) -> list[int]:
    """
    Forth evaluator.
    """
    *definitions, lst_operations = input_data
    user_defined: dict[str, str] = {}
    for definition in definitions:
        _, word, *substitution, _ = definition.lower().split()
        if is_int(word):
            raise ValueError("illegal operation")
        user_defined[word] = " ".join(
            user_defined.get(instrc, instrc) for instrc in substitution
        )
    instructions: list[str] = lst_operations.lower().split()
    stack = Stack()
    while instructions:
        instruction = instructions.pop(0)
        if instruction[0] == ":":
            raise ValueError("illegal operation")
        if is_int(instruction):
            stack.add(int(instruction))
        elif instruction in user_defined:
            instructions = user_defined[instruction].split() + instructions
        else:
            try:
                OPERATIONS[instruction](stack)
            except KeyError as no_op:
                raise ValueError("undefined operation") from no_op
    return stack.get_ints()

"""
https://exercism.org/tracks/python/exercises/circular-buffer
"""

import queue
from typing import Generic, TypeVar


class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """


GenericT = TypeVar("GenericT")


class CircularBuffer(Generic[GenericT]):
    """
    Circular Buffer using a Queue.
    """

    def __init__(self, capacity: int):
        self.buffer: queue.Queue[GenericT] = queue.Queue(maxsize=capacity)

    def read(self) -> GenericT:
        """
        Get an element from the buffer. Raise exception if empty.
        """
        try:
            return self.buffer.get_nowait()
        except queue.Empty as ex:
            raise BufferEmptyException("Circular buffer is empty") from ex

    def write(self, data: GenericT) -> None:
        """
        Put an element into the buffer. Raise exception if full.
        """
        try:
            self.buffer.put_nowait(data)
        except queue.Full as ex:
            raise BufferFullException("Circular buffer is full") from ex

    def overwrite(self, data: GenericT) -> None:
        """
        Put an element into the buffer.
        If the buffer is full, pop the oldest the element, and put the new element.
        """
        if self.buffer.full():
            self.buffer.get_nowait()
        self.write(data)

    def clear(self) -> None:
        """
        Clear the buffer.
        """
        while not self.buffer.empty():
            self.buffer.get_nowait()

"""Task: The function `add` accepts two arguments and returns a value, they all have the same type."""
from typing import TypeVar

T = TypeVar('T')


def add(a: T, b: T) -> T:
    """Generic function that adds two values of the same type."""
    ...
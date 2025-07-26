"""Task: Define a decorator that wraps a function and returns a function with the same signature."""
from typing import Callable, Any


def decorator[T: Callable[..., Any]](func: T) -> T:
    return func

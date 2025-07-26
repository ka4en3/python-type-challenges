"""Task: Define a decorator that wraps a function and returns a function with the same signature."""
from typing import Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])


def decorator(func: F) -> F:
    """Decorator that preserves function signature."""
    return func
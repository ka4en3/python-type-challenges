"""Task: foo only accepts literal 'left' and 'right' as its argument."""
from typing import Literal


def foo(direction: Literal["left", "right"]) -> None:
    """Function that accepts only 'left' or 'right' literals."""
    pass
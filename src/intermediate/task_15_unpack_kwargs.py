"""Task: `foo` expects two keyword arguments - `name` of type `str`, and `age` of type `int`."""
from typing import TypedDict, Unpack


class Person(TypedDict):
    """TypedDict for unpacking kwargs."""
    name: str
    age: int


def foo(**kwargs: Unpack[Person]) -> None:
    """Function with typed kwargs."""
    pass
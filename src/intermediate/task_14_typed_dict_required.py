"""Task: Define a class `Person` with only `name` required."""
from typing import TypedDict, Required, NotRequired


class Person(TypedDict):
    """TypedDict with mixed required/optional fields."""
    name: Required[str]
    age: NotRequired[int]
    gender: NotRequired[str]
    address: NotRequired[str]
    email: NotRequired[str]
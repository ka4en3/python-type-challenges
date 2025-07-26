"""Task: Define a class `Student` with optional school field."""
from typing import TypedDict, NotRequired


class Student(TypedDict):
    name: str
    age: int
    school: NotRequired[str]
"""Task: `foo` takes keyword arguments of type integer or string."""
from typing import Union


def foo(**kwargs: Union[int, str]) -> None:
    """Function that accepts keyword arguments of type int or str."""
    pass
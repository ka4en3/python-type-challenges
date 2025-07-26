"""Task: `return_self` should return an instance of the same type as the current enclosed class."""
import typing


class Foo:
    """Class with method returning Self."""
    
    def return_self(self) -> typing.Self:
        """Return instance of the same type."""
        ...
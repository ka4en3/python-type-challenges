"""Task: Annotate a function `execute_query` which runs SQL, but also can prevent SQL injection attacks."""
from typing import LiteralString, Iterable


def execute_query(sql: LiteralString, parameters: Iterable[str] = ...) -> None:
    """Execute SQL query safely."""
    ...
from typing import List

from .column import Column

class Table:
    columns: List[Column]

    def __init__(self, name: str) -> None:
        self.name = name

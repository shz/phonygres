from typing import List

from .column import Column

class Table:
    columns: List[Column]

    def __init__(self, name: str, columns: List[Column]) -> None:
        self.name = name
        self.columns = columns

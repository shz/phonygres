from typing import Optional

from .data_types import DataType

class Column:
    name: str
    data_type: DataType
    collate: Optional[str]

    def __init__(self, name: str, data_type: DataType, collate: Optional[str] = None) -> None:
        self.name = name
        self.data_type = data_type
        self.collate = collate

    def __repr__(self):
        return f'Column({self.name}, {self.data_type.__class__.__name__})'

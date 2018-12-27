from typing import Optional

class Column:
    name: str
    data_type: str # TODO - formalize
    collate: Optional[str]

    def __init__(self, name: str, data_type: str, collate: Optional[str] = None) -> None:
        self.name = name
        self.data_type = data_type
        self.collate = collate

    def __repr__(self):
        return f'Column({self.name}, {self.data_type})'

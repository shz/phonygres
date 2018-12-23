from typing import List, Union, NamedTuple

from ..ddl import Column

class CreateTable(NamedTuple):
    name: str
    if_not_exists: bool
    columns: List[Column]

CreateStatement = Union[CreateTable]

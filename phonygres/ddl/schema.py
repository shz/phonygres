from typing import Dict

from .table import Table
from ..errors import PhonygresError

class Schema:
    name: str
    tables: Dict[str, Table]

    def __init__(self, name: str) -> None:
        self.name = name
        self.tables = {}

    def add_table(self, table: Table) -> None:
        if table.name in self.tables:
            raise PhonygresError('42P07', f'relation "{table.name}" already exists')

        self.tables[table.name] = table

    def drop_table(self, table: Table) -> None:
        if table.name not in self.tables:
            raise PhonygresError('42P01', f'relation "{table.name}" does not exist')

        del self.tables[table.name]

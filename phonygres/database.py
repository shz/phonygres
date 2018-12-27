from typing import Dict

from .ddl import Schema
from .parser import parse_sql
from .engine import execute

class Database:
    schemas: Dict[str, Schema]

    def __init__(self):
        self.schemas = {}

    def execute(self, sql: str):
        for statement in parse_sql(sql):
            execute(statement, None) # TODO

        # raise Exception('no')

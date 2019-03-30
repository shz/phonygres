from typing import Dict

from .ddl import Schema

class Database:
    schemas: Dict[str, Schema]

    def __init__(self):
        self.schemas = {
            'public': Schema('public'),
        }

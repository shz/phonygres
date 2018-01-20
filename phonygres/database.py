from typing import Dict, Tuple

from sqlparse import parse
from sqlparse.sql import Statement
from sqlparse.tokens import Keyword

from .ddl import Schema
from .errors import PhonygresError
from .util import skip_whitespace

class Database:
    schemas: Dict[str, Schema]

    def __init__(self):
        self.schemas = {}

    def execute(self, sql: str):
        ast: Tuple[Statement] = parse(sql)

        for statement in ast:
            t = statement.get_type()
            tokens = list(skip_whitespace(statement))

            # Skip chunks of whitespace, but if there's real meat and
            # it can't be parsed, panic.
            if t == 'UNKNOWN':
                if len(tokens) == 0:
                    continue
                raise PhonygresError('42601', f'syntax error at or near "{tokens[0]}"')
            elif t == 'CREATE':
                print(tokens)
                if tokens[1].match(Keyword, 'TABLE'):
                    pass # TODO - Here we are
                else:
                    raise PhonygresError('42601', f'syntax error at or near "{tokens[1]}"')

            statement._pprint_tree()

        # raise Exception('no')

from typing import Optional, Tuple, List, Iterator, Dict

from sqlparse import parse as sql_parse
from sqlparse.sql import Statement as ParseStatement, Token
from sqlparse.tokens import Keyword

from .util import StatementIter
from .parse_create import parse_create
from ..ast import Statement
from ..errors import PhonygresError


def parse_sql(sql: str) -> List[Statement]:
    parse_ast: Tuple[ParseStatement] = sql_parse(sql)
    statements: List[Statement] = []

    for statement in parse_ast:
        iter = StatementIter(statement)

        # statement._pprint_tree()

        parsed = parse_statement(iter)
        if parsed is not None:
            statements.append(parsed)

    return statements

def parse_statement(iter: StatementIter) -> Optional[Statement]:
    t = iter.next_opt()
    if t is None:
        return None

    if t == 'CREATE':
        return parse_create(iter)
    else:
        raise PhonygresError('42601', f'syntax error at or near "{t}"')


from typing import Optional, Tuple, List

from sqlparse import parse as sql_parse
from sqlparse.sql import Statement as ParseStatement

from .util import StatementIter
from .parse_create import parse_create
from ..ast import Statement
from ..errors import PhonygresError


def parse_sql(sql: str) -> List[Statement]:
    parse_ast: Tuple[ParseStatement] = sql_parse(sql)
    statements: List[Statement] = []

    for statement in parse_ast:
        it = StatementIter(statement)

        statement._pprint_tree()

        parsed = parse_statement(it)
        if parsed is not None:
            statements.append(parsed)

    return statements

def parse_statement(it: StatementIter) -> Optional[Statement]:
    t = it.next_opt()
    if t is None:
        return None

    if t.normalized == 'CREATE':
        return parse_create(it)
    else:
        raise PhonygresError('42601', f'syntax error at or near "{t}"')

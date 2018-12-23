from typing import List

from .util import StatementIter
from ..errors import PhonygresError
from ..ast import CreateStatement, CreateTable
from ..ddl import Column

def parse_create(it: StatementIter) -> CreateStatement:
    t = it.next()

    # Postgres has a couple possible flags for creating things that
    # we're basically just going to ignore.
    while t in ['GLOBAL', 'LOCAL', 'TEMPORARY', 'TEMP', 'UNLOGGED']:
        t = it.next()

    if t == 'ACCESS':
        it.assert_next('METHOD')
        return None
    elif t == 'AGGREGATE':
        raise NotImplementedError()
    elif t == 'CAST':
        raise NotImplementedError()
    elif t == 'COLLATION':
        raise NotImplementedError()
    elif t == 'CONVERSION':
        raise NotImplementedError()
    elif t == 'DATABASE':
        raise NotImplementedError()
    elif t == 'DOMAIN':
        raise NotImplementedError()
    elif t == 'EVENT':
        raise NotImplementedError()
    elif t == 'EXTENSION':
        raise NotImplementedError()
    elif t == 'FOREIGN':
        raise NotImplementedError()
    elif t == 'TABLE':
        return parse_create_table(it)
    else:
        raise PhonygresError('42601', f'syntax error at or near "{t}"')

def parse_create_table(it: StatementIter) -> CreateTable:
    if_not_exists = False
    columns: List[Column] = []

    t = it.next()
    if t == 'IF NOT EXISTS':
        if_not_exists = True
        t = it.next()

    statement = CreateTable(
        name=t,
        if_not_exists=if_not_exists,
        columns=columns
    )

    return statement

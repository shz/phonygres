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
        it.assert_next('TRIGGER')
        raise NotImplementedError()
    elif t == 'EXTENSION':
        raise NotImplementedError()
    elif t == 'FOREIGN':
        raise NotImplementedError()
    elif t == 'FUNCTION':
        raise NotImplementedError()
    elif t == 'GROUP':
        raise NotImplementedError()
    elif t == 'INDEX':
        raise NotImplementedError()
    elif t == 'LANGUAGE':
        raise NotImplementedError()
    elif t == 'MATERIALIZED':
        it.assert_next('VIEW')
        raise NotImplementedError()
    elif t == 'OPERATOR':
        raise NotImplementedError()
    elif t == 'POLICY':
        raise NotImplementedError()
    elif t == 'PROCEDURE':
        raise NotImplementedError()
    elif t == 'PUBLICATION':
        raise NotImplementedError()
    elif t == 'ROLE':
        raise NotImplementedError()
    elif t == 'RULE':
        raise NotImplementedError()
    elif t == 'SCHEMA':
        raise NotImplementedError()
    elif t == 'SEQUENCE':
        raise NotImplementedError()
    elif t == 'SERVER':
        raise NotImplementedError()
    elif t == 'STATISTICS':
        raise NotImplementedError()
    elif t == 'SUBSCRIPTION':
        raise NotImplementedError()
    elif t == 'TABLE':
        return parse_create_table(it)
    elif t == 'TABLESPACE':
        raise NotImplementedError()
    elif t == 'TEXT':
        raise NotImplementedError()
    elif t == 'TRANSFORM':
        raise NotImplementedError()
    elif t == 'TRIGGER':
        raise NotImplementedError()
    elif t == 'TYPE':
        raise NotImplementedError()
    elif t == 'USER':
        raise NotImplementedError()
    elif t == 'VIEW':
        raise NotImplementedError()
    else:
        raise PhonygresError('42601', f'syntax error at or near "{t}"')

def parse_create_table(it: StatementIter) -> CreateTable:
    if_not_exists = False

    name = it.next()
    if name == 'IF NOT EXISTS':
        if_not_exists = True
        name = it.next()

    statement = CreateTable(
        name=name,
        if_not_exists=if_not_exists,
        columns=parse_columns(it)
    )

    return statement

def parse_columns(it: StatementIter) -> List[Column]:
    return []

from typing import cast, List, Any

from sqlparse import tokens, sql

from .util import StatementIter
from ..errors import PhonygresError
from ..ast import CreateStatement, CreateTable
from ..ddl import Column
from ..ddl.data_types import aliases, DataType

def parse_create(it: StatementIter) -> CreateStatement:
    t = it.next()

    # Postgres has a couple possible flags for creating things that
    # we're basically just going to ignore.
    while t.normalized in ['GLOBAL', 'LOCAL', 'TEMPORARY', 'TEMP', 'UNLOGGED']:
        t = it.next()

    tv = t.normalized
    if tv == 'ACCESS':
        it.assert_next('METHOD')
        return None
    elif tv == 'AGGREGATE':
        raise NotImplementedError()
    elif tv == 'CAST':
        raise NotImplementedError()
    elif tv == 'COLLATION':
        raise NotImplementedError()
    elif tv == 'CONVERSION':
        raise NotImplementedError()
    elif tv == 'DATABASE':
        raise NotImplementedError()
    elif tv == 'DOMAIN':
        raise NotImplementedError()
    elif tv == 'EVENT':
        it.assert_next('TRIGGER')
        raise NotImplementedError()
    elif tv == 'EXTENSION':
        raise NotImplementedError()
    elif tv == 'FOREIGN':
        raise NotImplementedError()
    elif tv == 'FUNCTION':
        raise NotImplementedError()
    elif tv == 'GROUP':
        raise NotImplementedError()
    elif tv == 'INDEX':
        raise NotImplementedError()
    elif tv == 'LANGUAGE':
        raise NotImplementedError()
    elif tv == 'MATERIALIZED':
        it.assert_next('VIEW')
        raise NotImplementedError()
    elif tv == 'OPERATOR':
        raise NotImplementedError()
    elif tv == 'POLICY':
        raise NotImplementedError()
    elif tv == 'PROCEDURE':
        raise NotImplementedError()
    elif tv == 'PUBLICATION':
        raise NotImplementedError()
    elif tv == 'ROLE':
        raise NotImplementedError()
    elif tv == 'RULE':
        raise NotImplementedError()
    elif tv == 'SCHEMA':
        raise NotImplementedError()
    elif tv == 'SEQUENCE':
        raise NotImplementedError()
    elif tv == 'SERVER':
        raise NotImplementedError()
    elif tv == 'STATISTICS':
        raise NotImplementedError()
    elif tv == 'SUBSCRIPTION':
        raise NotImplementedError()
    elif tv == 'TABLE':
        return parse_create_table(it)
    elif tv == 'TABLESPACE':
        raise NotImplementedError()
    elif tv == 'TEXT':
        raise NotImplementedError()
    elif tv == 'TRANSFORM':
        raise NotImplementedError()
    elif tv == 'TRIGGER':
        raise NotImplementedError()
    elif tv == 'TYPE':
        raise NotImplementedError()
    elif tv == 'USER':
        raise NotImplementedError()
    elif tv == 'VIEW':
        raise NotImplementedError()
    else:
        raise PhonygresError('42601', f'syntax error at or near "{t.value}"')

def parse_create_table(it: StatementIter) -> CreateTable:
    if_not_exists = False

    name = it.next()
    if name.ttype == tokens.Keyword:
        if name.normalized != 'IF':
            raise PhonygresError('42601', f'syntax error at or near "{name.value}"')
        it.assert_next('NOT')
        it.assert_next('EXISTS')
        if_not_exists = True
        name = it.next()

    statement = CreateTable(
        name=name.value,
        if_not_exists=if_not_exists,
        columns=parse_columns(it)
    )

    return statement

def parse_columns(it: StatementIter) -> List[Column]:
    # Column definitions always come wrapped in parenthesis
    root = it.next()
    if not isinstance(root, sql.Parenthesis):
        raise PhonygresError('42601', f'syntax error at or near "{root.value}"')

    columns = []
    sub_it = StatementIter(cast(sql.Statement, root))

    while True:
        # Parse until we run out
        name = sub_it.next_opt()
        if name is None:
            break

        # Table constraints follow the regular list of columns, parse them
        # separately and then finish.
        if not isinstance(name, sql.Identifier):
            break # TODO

        # Parse the data type
        data_type_parts: List[sql.Token] = []
        args: List[Any] = [] # TODO - parse these out
        while sub_it.has_next() and sub_it.peek().ttype is tokens.Name.Builtin:
            data_type_parts.append(sub_it.next())
        data_type_str = ' '.join([t.normalized for t in data_type_parts]).lower()
        # See: https://github.com/python/mypy/issues/4997
        data_type: DataType = aliases.get(data_type_str)(*args) # type: ignore
        if data_type is None:
            raise PhonygresError('42704', f'type "{data_type_str}" does not exist')

        # Parse the optional collation flag
        collate = None
        if sub_it.has_next() and sub_it.peek().normalized == 'COLLATE':
            sub_it.next() # Consume peeked value
            collate = sub_it.next()

        # TODO - parse column constraints

        # Assemble the column entry
        columns.append(Column(
            name.value,
            data_type,
            collate.normalized if collate is not None else None
        ))

    return columns

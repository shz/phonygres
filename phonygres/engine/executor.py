# pylint: disable=function-redefined, wildcard-import, unused-wildcard-import

from typing import Dict, Type, Any, Callable

from ..ast import *
from ..transaction import Transaction
from ..database import Database
from ..ddl import Table

visitors: Dict[Type, Callable[[Transaction, Statement, Database], Any]] = {
    # TX
    StartTransaction: lambda tx, st, db: None,
    Commit: lambda tx, st, db: None,

    # DDL
    CreateTable: lambda tx, st, db: db.schemas[tx.current_schema].add_table(
        Table(st.name, st.columns)),
}

def execute(tx: Transaction, statement: Statement, target: Database) -> Any:
    return visitors[statement.__class__](tx, statement, target)

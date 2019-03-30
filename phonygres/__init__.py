from .database import Database
from .errors import PhonygresError
from .parser import parse_sql
from .transaction import Transaction
from .engine import execute

def execute_sql(db: Database, sql: str):
    tx = None
    for statement in parse_sql(sql):
        tx = Transaction()
        execute(tx, statement, db)
        if tx.autocommit:
            tx.commit()


        # raise Exception('no')

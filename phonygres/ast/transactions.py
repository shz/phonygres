from enum import Enum
from typing import NamedTuple, Union

class IsolationLevel(Enum):
    serializable = 'SERIALIZABLE'
    repeatable_read = 'REPEATABLE READ'
    read_committed = 'READ COMMITTED'
    read_uncommited = 'READ UNCOMMITTED'

class StartTransaction(NamedTuple):
    deferrable: bool
    read_only: bool
    isolation_level: IsolationLevel

class Commit:
    pass

class Rollback:
    pass

class Savepoint(NamedTuple):
    name: str

class RollbackToSavepoint(NamedTuple):
    name: str

class ReleaseSavepoint(NamedTuple):
    name: str

TransactionStatement = Union[
    StartTransaction,
    Commit,
    Rollback,
    Savepoint,
    RollbackToSavepoint,
    ReleaseSavepoint,
]

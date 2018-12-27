from typing import Iterator, Optional

from sqlparse.sql import Token, Statement
from sqlparse.tokens import Punctuation

from ..errors import PhonygresError

class StatementIter:
    statement: Statement
    iter: Iterator[Token]
    peek_val: Optional[Token]

    def __init__(self, statement: Statement) -> None:
        self.statement = statement
        self.peek_val = None
        self.iter = self._iter()

    def _iter(self) -> Iterator[Token]:
        idx = 0

        while True:
            # This gets a bit funky due to the co-routine nature of this
            # class' usage.  It's possible that while we're yielding, the
            # peek_val gets set again.
            while self.peek_val is not None:
                v = self.peek_val
                self.peek_val = None
                yield v

            idx, t = self.statement.token_next(idx, skip_ws=True, skip_cm=True)

            if t is None:
                return
            elif t.ttype == Punctuation:
                continue
            else:
                yield t

    def peek(self) -> Token:
        if self.peek_val is not None:
            return self.peek_val

        self.peek_val = self.next()
        return self.peek_val

    def next(self) -> Token:
        try:
            return next(self.iter)
        except StopIteration:
            raise PhonygresError('42601', f'syntax error at end of input')

    def next_opt(self) -> Optional[Token]:
        try:
            return next(self.iter)
        except StopIteration:
            return None

    def has_next(self) -> bool:
        t = self.next_opt()
        if t is None:
            return False
        else:
            self.peek_val = t
            return True

    def assert_next(self, value: str):
        t = self.next()
        if t.normalized != value:
            raise PhonygresError('42601', f'syntax error at or near "{t.value}"')

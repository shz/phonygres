from typing import Iterator, Optional

from sqlparse.sql import Token, TokenList, Statement

from ..errors import PhonygresError

class StatementIter:
    statement: Statement
    iter: Iterator[str]

    def __init__(self, statement: Statement) -> None:
        self.statement = statement
        self.iter = self._iter()

    def _iter(self) -> Iterator[str]:
        tokens = skip_whitespace(self.statement)
        for t in tokens:
            yield t.value

    def next(self) -> str:
        try:
            return next(self.iter)
        except StopIteration:
            raise PhonygresError('42601', f'syntax error at end of input')

    def next_opt(self) -> Optional[str]:
        try:
            return next(self.iter)
        except StopIteration:
            return None

    def assert_next(self, value: str):
        t = self.next()
        if t != value:
            raise PhonygresError('42601', f'syntax error at or near "{t}"')


def skip_whitespace(tokens: TokenList) -> Iterator[Token]:
    '''
    Converts a TokenList into the equivalent iterator of Token objects,
    but with all whitespace removed.
    '''
    for token in tokens:
        if not token.is_whitespace:
            yield token

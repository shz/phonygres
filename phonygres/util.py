from typing import Iterator

from sqlparse.sql import Token, TokenList

def skip_whitespace(tokens: TokenList) -> Iterator[Token]:
    '''
    Converts a TokenList into the equivalent iterator of Token objects,
    but with all whitespace removed.
    '''
    for token in tokens:
        if not token.is_whitespace:
            yield token

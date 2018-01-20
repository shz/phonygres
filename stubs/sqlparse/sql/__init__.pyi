from typing import Optional, Iterator

class Token:
    is_whitespace: bool

    def match(self, ttype: str, values: str) -> bool: ...

class TokenList(Token):
    def __iter__(self) -> Iterator[Token]: ...

class Statement(TokenList):
    def get_type(self) -> str: ...
    def _pprint_tree(self) -> None: ...

class Identifier(TokenList):
    def is_wildcard(self) -> bool: ...
    def get_typecast(self) -> Optional[str]: ...
    def get_ordering(self) -> Optional[str]: ...
    def get_array_indices(self) -> Iterator[int]: ...

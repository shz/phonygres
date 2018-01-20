from typing import Tuple, Any

from .sql import Statement

def parse(sql: str, encoding: str = None) -> Tuple[Statement]: ...

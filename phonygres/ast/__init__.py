# pylint: disable=wildcard-import

from typing import Union

from .create import *
from .transactions import *


Statement = Union[
    CreateStatement,
    TransactionStatement,
]

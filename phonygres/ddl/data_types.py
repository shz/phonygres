from typing import Any, List, Dict, Type

class DataType:
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DataType):
            return False

        return self.__dict__ == other.__dict__

class Unsupported:
    def __new__(cls, *args, **kwargs):
        # Can't raise NotImplemented due to pylint, hah
        raise Exception('Unsupported')

class BigInt(DataType):
    pass

class BigSerial(DataType, Unsupported):
    pass

class Bit(DataType, Unsupported):
    length: int

    def __init__(self, n: int) -> None:
        self.length = n

class BitVarying(DataType, Unsupported):
    length: int

    def __init__(self, n: int) -> None:
        self.length = n

class Boolean(DataType):
    pass

class Box(DataType, Unsupported):
    pass

class ByteA(DataType, Unsupported):
    pass

class Character(DataType, Unsupported):
    length: int

    def __init__(self, n: int) -> None:
        self.length = n

class CharacterVarying(DataType):
    pass

class CIDR(DataType, Unsupported):
    pass

class Circle(DataType, Unsupported):
    pass

class Date(DataType, Unsupported):
    pass

class DoublePrecision(DataType, Unsupported):
    pass

class INet(DataType, Unsupported):
    pass

class Integer(DataType):
    pass

class Interval(DataType, Unsupported):
    fields: List[Any]
    p: Any

    def __init__(self, fields: List[Any], p: Any) -> None:
        self.fields = fields
        self.p = p

class JSON(DataType, Unsupported):
    pass

class JSONB(DataType, Unsupported):
    pass

class Line(DataType, Unsupported):
    pass

class LSeg(DataType, Unsupported):
    pass

class MacAddr(DataType, Unsupported):
    pass

class MacAddr8(DataType, Unsupported):
    pass

class Money(DataType, Unsupported):
    pass

class Numeric(DataType, Unsupported):
    p: int
    s: int

    def __init__(self, p: int, s: int) -> None:
        self.p = p
        self.s = s

class Path(DataType, Unsupported):
    pass

class PGLSN(DataType, Unsupported):
    pass

class Point(DataType, Unsupported):
    pass

class Polygon(DataType, Unsupported):
    pass

class Real(DataType, Unsupported):
    pass

class SmallInt(DataType, Unsupported):
    pass

class SmallSerial(DataType, Unsupported):
    pass

class Serial(DataType, Unsupported):
    pass

class Text(DataType, Unsupported):
    pass

class Time(DataType, Unsupported):
    p: Any
    with_time_zone: bool

    def __init__(self, p: Any, with_time_zone: bool) -> None:
        self.p = p
        self.with_time_zone = with_time_zone

class Timestamp(DataType, Unsupported):
    p: Any
    with_time_zone: bool

    def __init__(self, p: Any, with_time_zone: bool) -> None:
        self.p = p
        self.with_time_zone = with_time_zone

class TSQuery(DataType, Unsupported):
    pass

class TSVector(DataType, Unsupported):
    pass

class TXIDSnapshot(DataType, Unsupported):
    pass

class UUID(DataType, Unsupported):
    pass

class XML(DataType, Unsupported):
    pass

aliases: Dict[str, Type[DataType]] = {
    'bigint': BigInt,
    'int8': BigInt,
    'bigserial': BigSerial,
    'serial8': BigSerial,
    'bit': Bit,
    'bit varying': BitVarying,
    'varbit': BitVarying,
    'boolean': Boolean,
    'bool': Boolean,
    'box': Box,
    'bytea': ByteA,
    'character': Character,
    'char': Character,
    'character varying': CharacterVarying,
    'varchar': CharacterVarying,
    'cidr': CIDR,
    'circle': Circle,
    'date': Date,
    'double precision': DoublePrecision,
    'float8': DoublePrecision,
    'inet': INet,
    'integer': Integer,
    'int': Integer,
    'int4': Integer,
    'interval': Interval,
    'json': JSON,
    'jsonb': JSONB,
    'line': Line,
    'lseg': LSeg,
    'macaddr': MacAddr,
    'macaddr8': MacAddr8,
    'money': Money,
    'numeric': Numeric,
    'decimal': Numeric,
    'path': Path,
    'pg_lsn': PGLSN,
    'point': Point,
    'polygon': Polygon,
    'real': Real,
    'float4': Real,
    'smallint': SmallInt,
    'int2': SmallInt,
    'smallserial': SmallSerial,
    'serial2': SmallSerial,
    'serial': Serial,
    'serial4': Serial,
    'text': Text,
    'time': Time,
    'time without time zone': Time,
    'time with time zone': Time,
    'timetz': Time,
    'timestamp': Timestamp,
    'timestamp without time zone': Timestamp,
    'timestamp with time zone': Timestamp,
    'timestamptz': Timestamp,
    'tsquery': TSQuery,
    'tsvector': TSVector,
    'txid_snapshot': TXIDSnapshot,
    'uuid': UUID,
    'xml': XML,
}

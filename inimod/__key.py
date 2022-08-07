from dataclasses import dataclass


@dataclass
class Key:
    _type: str
    _key: str
    _value: any

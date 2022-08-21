from dataclasses import dataclass
from inimod.token import Token
from inimod.__key import Key


@dataclass
class Structure:
    _type: str
    _id: str
    _keys: list[Key]



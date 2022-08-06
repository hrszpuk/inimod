from dataclasses import dataclass
from inimod.__token import Token


@dataclass
class Structure:
    _type: str
    tokens: list[Token]

    def __repr__(self):
        return f"(Type: {self._type}, {self.tokens})"

    def __str__(self):
        return self.__repr__()

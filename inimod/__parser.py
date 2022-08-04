from dataclasses import dataclass
import __exceptions as __internal__


@dataclass
class Token:
    _type: str
    value: any

    def __repr__(self):
        return f"({self._type}, {self.value})"

    def __str__(self):
        return self.__repr__()


class Parser:

    def __init__(self, filename: str):
        self.__tokens = self.__lex(Parser.__handle_file(filename))

    @classmethod
    def __handle_file(cls, filename: str) -> str:
        try:
            file = open(filename, "r")
            contents = file.read()
        except FileNotFoundError as err:
            raise __internal__.FileHandleException
        except OSError as err:
            raise __internal__.FileHandleException
        except Exception as err:
            raise err
        return contents

    def __lex(self, __raw: str) -> list[Token]:
        return []

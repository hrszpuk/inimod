from dataclasses import dataclass
from inimod.__exceptions import FileHandleException
from inimod.__structure import *


class Parser:

    def __init__(self, filename: str):
        self.delimiter = "="  # symbol used to denote key/value declaration
        self.tokens = self.__lex(Parser.__handle_file(filename))

    @classmethod
    def __handle_file(cls, filename: str) -> str:
        try:
            file = open(filename, "r")
            contents: str = file.read()
        except FileNotFoundError as err:
            raise FileHandleException(str(err))
        except OSError as err:
            raise FileHandleException(str(err))
        except Exception as err:
            raise err
        return contents

    def __lex(self, __raw: str) -> list[Token]:
        """
        __lex handles generating tokens for the parser.
        Tokens are ways of identifying different "things" in the ini code.
        Tokens:
         - LEFT_BRACKET : "["
         - RIGHT_BRACKET : "]"
         - IDENTIFIER : "cat", "hello123", etc ([a-zA-Z0-9]+)
         - INTEGER : any while numbers
         - REAL : any floating point numbers
         - STRING : strings of characters (starting with " or ')
         - IP_ADDR : 192.84.12.4, etc (xxx.xxx.xxx.xxx)
         - DELIMITER : defaults to "=" but can be changed
         - COMMENT : any line starting with ";" or "#"
        """
        lexical_tokens: list[Token] = []
        error_buffer: str = ""
        flush = lambda: lexical_tokens.append(Token("UnknownTokenException", error_buffer))
        index: int = 0
        length: int = len(__raw)
        while index < length:
            if __raw[index] == "[":
                if error_buffer != "":
                    flush()
                lexical_tokens.append(Token("LEFT_BRACKET", "["))
                index += 1
            elif __raw[index] == "]":
                if error_buffer != "":
                    flush()
                lexical_tokens.append(Token("RIGHT_BRACKET", "]"))
                index += 1
            elif __raw[index] == self.delimiter:
                if error_buffer != "":
                    flush()
                lexical_tokens.append(Token("DELIMITER", self.delimiter))
                index += 1
            elif __raw[index] == '"' or __raw[index] == "'":
                if error_buffer != "":
                    flush()
                symbol: str = __raw[index]
                buffer: str = ""
                index += 1
                while index < length and __raw[index] != symbol:
                    buffer += __raw[index]
                    index += 1
                lexical_tokens.append(Token("STRING", buffer))
                index += 1
            elif __raw[index].isdigit():
                if error_buffer != "":
                    flush()
                buffer: str = __raw[index]
                index += 1
                _type: str = "INTEGER"
                dot_count: int = 0
                while index < length and (__raw[index].isdigit() or __raw[index] == "."):
                    if __raw[index] == ".":
                        dot_count += 1
                        _type = "REAL" if dot_count == 1 else "IP_ADDR"
                    buffer += __raw[index]
                    index += 1
                if _type == "IP_ADDR" and dot_count != 3:
                    lexical_tokens.append(Token("UnknownTokenException", "An IP Address cannot have more than 3 dots"))
                else:
                    lexical_tokens.append(Token(_type, int(buffer) if _type == "INTEGER" else float(buffer)))
            elif __raw[index].isalpha():
                if error_buffer != "":
                    flush()
                buffer: str = __raw[index]
                index += 1
                while index < length and __raw[index].isalnum():
                    buffer += __raw[index]
                    index += 1
                lexical_tokens.append(Token("IDENTIFIER", buffer))
            elif __raw[index] == ";" or __raw[index] == "#":
                if error_buffer != "":
                    flush()
                buffer: str = ""
                index += 1
                while index < length and __raw[index] != "\n":
                    buffer += __raw[index]
                    index += 1
                lexical_tokens.append(Token("COMMENT", buffer))
            elif __raw[index] in " \n\t\v":
                if error_buffer != "":
                    flush()
                index += 1
            else:
                error_buffer += __raw[index]
                index += 1
        return lexical_tokens

    def __parse(self):
        """
        __parse handles generating structures from a series of tokens.
        The tokens are generated in __lex, and __parse recognises patterns in these tokens.
        Structures:
            - Section: LEFT_BRACKET IDENTIFIER RIGHT_BRACKET
            - Key: IDENTIFIER DELIMITER Expr
            - Expr: NUMBER | STRING | IP_ADDR

        """
        index: int = 0
        length = len(self.tokens)
        while index < length:
            if self.tokens[index].type == "LEFT_BRACKET":
                self.__parse_section()
            else:
                raise Exception

    def __parse_section(self):
        """
        Handles parsing ini sections: [section example]
        """
        pass

    def __parse_key(self):
        """
        Handles parsing ini keys: example_key = 100
        """
        pass

    def __parse_expr(self):
        """
        Handles parsing expressions: 100, "hello", 1.1.1.1
        """
        pass


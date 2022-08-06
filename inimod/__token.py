

class Token:
    """
    Stores the necessary information for a lexical token.
    """
    def __init__(self, _type: str, _value: any):
        self.__type: str
        self.__value: any
        self.__allowed_types = [
            "LEFT_BRACKET",
            "RIGHT_BRACKET",
            "IDENTIFIER",
            "INTEGER",
            "REAL",
            "STRING",
            "IP_ADDR",
            "DELIMITER",
            "COMMENT",
        ]
        self.__type: str = _type
        self.__value: any = _value

    def __repr__(self):
        return f"({self.__type}, {self.__value})"

    def __str__(self):
        return self.__repr__()

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type: str):
        if new_type in self.__allowed_types:
            self.__type = new_type

    @property
    def value(self):
        return self.__value

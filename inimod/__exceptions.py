
class ParsingException(Exception):
    """
    An exception occurred during the parsing of an ini config file.
    """
    def __init__(self, message: str):
        super().__init__(message)


class UnknownTokenException(ParsingException):
    """
    An unknown token was found during the processing of an ini config file.
    This exception occurs when a token has not been described to the parser therefore it cannot be processed.

    **Ensure your config file(s) does not contain characters or symbols that are not part of the INI specification.**
    """
    def __init__(self, message: str):
        super().__init__(message)


class UnexpectedTokenException(ParsingException):
    """
    An **unexpected token** was found during the processing of an ini config file.
    This exception occurs when a token is found but **the parser was expecting a different set of tokens**.

    **This is often due to missing or incorrect syntax by the user (check your config file for incorrect syntax).**
    """
    def __init__(self, message: str):
        super().__init__(message)


class FileHandleException(ParsingException, FileNotFoundError):
    """
    An issue occurred opening or finding the ini config file specified.

    **Ensure your filename/path to the config file(s) is correct.**
    """
    def __init__(self, message: str):
        super().__init__(message)


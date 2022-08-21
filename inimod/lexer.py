from inimod import token


class Lexer:
    """
    __lex handles generating tokens for the parser.
        Tokens are ways of identifying different "things" in the ini code.
    """

    def __init__(self, code: str, delimiter: str = "="):
        self.code = code
        self.delimiter = delimiter
        self.tokens = []

    def analyse(self) -> list:
        index = 0
        length = len(self.code)

        while index < length:
            if self.code[index].isdigit():
                buffer = self.code[index]
                index += 1

                while index < length and self.code[index].isdigit():
                    buffer += self.code[index]
                    index += 1

                self.tokens.append(token.Token("INTEGER", buffer))

            elif self.code[index] == '"' or self.code[index] == "'":
                symbol = self.code[index]
                buffer = ""
                index += 1

                while index < length and self.code[index] != symbol:
                    buffer += self.code[index]
                    index += 1

                index += 1
                self.tokens.append(token.Token("STRING", buffer))

            elif self.code[index].isalpha():
                buffer = self.code[index]
                index += 1

                while index < length and (self.code[index].isalnum() or self.code[index] in "_-+ "):
                    buffer += self.code[index]
                    index += 1

                self.tokens.append(token.Token("IDENTIFIER", buffer))

            elif self.code[index] == "[":
                self.tokens.append(token.Token("LEFT_BRACKET", self.code[index]))
                index += 1

            elif self.code[index] == "]":
                self.tokens.append(token.Token("RIGHT_BRACKET", self.code[index]))
                index += 1

            elif self.code[index] == self.delimiter:
                self.tokens.append(token.Token("DELIMITER", self.code[index]))
                index += 1

            elif self.code[index] == ";" or self.code[index] == "#":
                while index < length and self.code[index] != "\n":
                    index += 1
                index += 1

            elif self.code[index] in " \n\t\v":
                index += 1

            else:
                print("Unexpected Character!")
                index += 1

        return self.tokens

from inimod.section_node import SectionNode
from inimod.key_node import KeyNode
from inimod.expression_node import ExpressionNode


class Parser:
    """

    """

    def __init__(self, tokens: list):
        self.tokens = tokens
        self.length = len(self.tokens)
        self.index = 0
        self.nodes = []

    def parse(self) -> list:
        while self.index < self.length:
            if self.tokens[self.index].value == "[":
                section = self.parse_section()
                if section != Exception:
                    self.nodes.append(section)
            elif self.tokens[self.index].type == "IDENTIFIER":
                key = self.parse_key()
                if key != Exception:
                    self.nodes.append(key)
            else:
                print(f"Unexpected Token: {self.tokens[self.index]}")
                self.index += 1

        return self.nodes

    def parse_section(self):
        if self.index+2 >= self.length:
            return Exception

        left = self.tokens[self.index]
        identifier = self.next()
        right = self.next()

        self.index += 1

        return SectionNode([left, identifier, right], identifier)

    def parse_key(self):
        if self.index+2 >= self.length:
            return Exception

        identifier = self.tokens[self.index]
        delimiter = self.next()
        expression = self.parse_expression()

        return KeyNode(identifier, delimiter, expression)

    def parse_expression(self):
        if self.index+1 >= self.length:
            return Exception

        literal = self.next()

        self.index += 1

        return ExpressionNode(literal)

    def next(self):
        if self.index+1 < self.length:
            self.index += 1
            return self.tokens[self.index]
        else:
            return Exception



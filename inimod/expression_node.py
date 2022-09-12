from inimod.node import Node
from inimod.token import Token


class ExpressionNode(Node):
    """

    """

    def __init__(self, literal: Token):
        super().__init__([literal])
        self.literal = literal.value
        if literal.type == "INTEGER":
            self.literal = int(literal.value)
        self.type = "EXPRESSION"


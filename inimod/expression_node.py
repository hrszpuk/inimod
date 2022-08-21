from inimod.node import Node
from inimod.token import Token


class ExpressionNode(Node):
    """

    """

    def __init__(self, literal: Token):
        super().__init__([literal])
        self.literal = literal
        self.value = self.literal.value


from inimod.node import Node
from inimod.token import Token


class KeyNode(Node):
    """

    """

    def __init__(self, identifier: Token, delimiter, expr_node):
        self.identifier = identifier
        self.delimiter = delimiter
        self.expr = expr_node
        self.type = "KEY"

        super().__init__([identifier, delimiter, expr_node])

from inimod.node import Node
from inimod.token import Token


class SectionNode(Node):
    """

    """


    def __init__(self, tokens: list, identifier: Token):
        super().__init__(tokens)
        self.identifier = identifier
        self.type = "SECTION"


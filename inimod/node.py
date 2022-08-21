class Node:
    """

    """

    def __init__(self, tokens: list):
        self.tokens = tokens

    def __repr__(self):
        return " ".join(token.value for token in self.tokens)

    def __str__(self):
        return self.__repr__()


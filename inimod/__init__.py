from inimod import __parser


def read(filename: str):
    x = __parser.Parser(filename)
    return x.tokens


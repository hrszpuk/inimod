
def test():
    import datetime

    print("Testing inimod")
    now = lambda: datetime.datetime.now().time()

    print(f"[{now()}] importing inimod")
    import inimod
    with open("test.ini", "r") as f:
        t = inimod.lexer.Lexer(f.read()).analyse()
        n = inimod.parser.Parser(t).parse()
        print(n)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("\"inimod\" is a Python library, please do not run it as a standalone script.")


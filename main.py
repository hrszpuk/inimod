
def test(filename):
    import datetime
    now = lambda: datetime.datetime.now().time()
    print(f"[{now()}] :: Reading \"{filename}\"")
    file = open(filename, 'r')
    contents = file.read()
    char_count = len(contents)
    line_count = len(contents.split("\n"))
    print(f"[{now()}] :: Read {line_count} line(s), {char_count} character(s)")

    print(f"[{now()}] :: Importing inimod")
    import inimod

    print(f"[{now()}] :: Conducting lexical analysis")
    tokens = inimod.lexer.Lexer(contents).analyse()
    bad_tokens = [token for token in tokens if token.type == 'BAD']
    print(f"[{now()}] !! Found {len(tokens)} tokens ({len(bad_tokens)} bad tokens)")
    print(f"[{now()}] :: Started parsing")
    nodes = inimod.parser.Parser(tokens).parse()
    print(f"[{now()}] :: Finished parsing")
    section_count = len([node for node in nodes if node.type == "SECTION"])
    key_count = len([node for node in nodes if node.type == "KEY"])
    print(f"[{now()}] !! Found {section_count} section(s) and {key_count} key(s)")
    print(f"[{now()}] :: Started binding")
    dict = inimod.bind(nodes)
    print(dict)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        if sys.argv[1] in ["--test", "test", "-t"]:
            test(sys.argv[2])
        else:
            print(f"inimod does not support the argument \"{sys.argv[2]}\"!")
    else:
        print("\"inimod\" is a Python library, please do not run it as a standalone script.")


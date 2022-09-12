

def load(code: str) -> dict:
    """
    description
    This function will take ini config structure and return a Python dictionary of said contents.
    Every "header" is converted to a dictionary key.
    Each dictionary key ("header") is a dictionary itself containing all the "header"'s "key"s.

    Any key declared before any section are declared (at the top of the file) will be placed in a dictionary key
    called "global".

    This is a simple wrapper function for user's convenience.
    Internally, this function will make calls to the other wrapper functions:
    lex() -> parse() -> bind()
    """
    from inimod.binder import bind
    return bind(parse(lex(code)))


def lex(code: str) -> list:
    """
    This function will take .ini config structure (usually read from a .ini config file) and return
    a list of all the tokens: Token(value, type) within the config.
    The output can be given to inimod.parse() which will convert the tokens into a list of node objects.

    This is a simple wrapper function for the user's convenience.
    Internally, this function will initialise a new Lexer object and call the analyse() method which will
    return a list of tokens generated from the ini code provided.
    """
    from inimod.lexer import Lexer
    return Lexer(code).analyse()


def parse(tokens: list) -> list:
    """
    This function will take a list of tokens (inimod.token.Token) and return a list of nodes (inimod.node.Node).
    The output can be given to inimod.bind() which will generate a Python dictionary from the nodes.

    This is a simple wrapper fucntion for the user's convenience.
    Internally, this function will initialise a new Parser object and call parse() which will
    return a list of nodes generated from the tokens provided.
    """
    from inimod.parser import Parser
    return Parser(tokens).parse()


def test(filename: str):
    """
    This function can be used to ensure inimod is working properly.
    This is generally used by the inimod developer (Remy) to test, but it is avaliable to the user if they
    wish to use it for whatever reason.

    To use test() simply provided a filename (of a .ini) and the file will be read with a Dictionary being generated.
    test() will output when different processes start and end, as well as the output (can be useful for finding issues).

    **Example:**

    import inimod

    inimod.test("example_test.ini")
    """
    import datetime
    now = lambda: datetime.datetime.now().time()

    # File opening and reading
    print(f"[{now()}] :: Reading \"{filename}\"")
    file = open(filename, 'r')
    contents = file.read()
    char_count = len(contents)
    line_count = len(contents.split("\n"))
    print(f"[{now()}] :: Read {line_count} line(s), {char_count} character(s)")

    # Importing inimod
    print(f"[{now()}] :: Importing inimod")
    from inimod.lexer import Lexer
    from inimod.parser import Parser
    from inimod.binder import bind

    # Lexing the file for Tokens
    print(f"[{now()}] :: Conducting lexical analysis")
    tokens = Lexer(contents).analyse()
    bad_tokens = [token for token in tokens if token.type == 'BAD']
    print(f"[{now()}] !! Found {len(tokens)} tokens ({len(bad_tokens)} bad tokens)")

    # Parsing the tokens for sections, keys, and expressions
    print(f"[{now()}] :: Started parsing")
    nodes = Parser(tokens).parse()
    print(f"[{now()}] :: Finished parsing")
    section_count = len([node for node in nodes if node.type == "SECTION"])
    key_count = len([node for node in nodes if node.type == "KEY"])
    print(f"[{now()}] !! Found {section_count} section(s) and {key_count} key(s)")

    # Converts the Parser output to a Python Dictionary
    print(f"[{now()}] :: Started binding")
    dictionary = bind(nodes)
    print(f"[{now()}] :: Finished binding")
    print(f"[{now()}] !! Generated Dictionary")

    # Asks if test user would like the dictionary in the terminal (pretty printed)
    if input(f"[{now()}] ?? Would you like to view Dictionary output [Y/n]").lower() in ("y", "yeah", "yes"):
        print("{")
        for section in dictionary.keys():
            print(f"    '{section}': " + "{")
            for key in dictionary[section]:
                print(f"        '{key}': {str(dictionary[section][key])},")
            print("    }, ")
        print("}")

    # Closing the file, and final output
    print(f"[{now()}] :: Closing \"{filename}\"")
    file.close()
    print(f"[{now()}] %% Finished!")

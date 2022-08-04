
def test():
    import datetime

    print("Testing inimod")
    now = lambda: datetime.datetime.now().time()

    print(f"[{now()}] importing inimod")
    import inimod


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("\"inimod\" is a Python library, please do not run it as a standalone script.")


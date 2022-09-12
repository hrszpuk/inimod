import inimod

with open("test.ini", 'r') as f:
    print(inimod.load(f.read()))


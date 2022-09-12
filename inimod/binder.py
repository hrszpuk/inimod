

def bind(nodes: list) -> dict:
    index = 0
    length = len(nodes)
    dictionary = {}
    current_section = "global"
    while index < length:
        if nodes[index].type == "SECTION":
            current_section = nodes[index].identifier.value
            dictionary[current_section] = {}
        elif nodes[index].type == "KEY":
            value = nodes[index].expr.literal
            if current_section not in dictionary.keys():
                dictionary[current_section] = {}
            dictionary[current_section][nodes[index].identifier.value] = value
        else:
            print("[DEV] You're trying to add new node types without binding them >:(")
        index += 1

    return dictionary

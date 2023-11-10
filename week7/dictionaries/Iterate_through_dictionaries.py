def pattern():
    sequence = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequence


def display_keys(data):
    print("Keys")
    for key in data:
        print(key)
    print()


def display_values(data):
    print("Values")
    for value in data.values():
        print(value)
    print()


def display_items(data):
    print("Pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")
    print()


def run():
    dictionary = pattern()
    print(f"Dictionary: \n{dictionary}")
    display_keys(dictionary)
    display_values(dictionary)
    display_keys(dictionary)


run()

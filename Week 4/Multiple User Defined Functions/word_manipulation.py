# Display word in box
def display_word_box(word):
    num_dashes = 4 + len(word)

    # Displays the word in a box
    print("-" * num_dashes)
    print(f"| {word} |")
    print("-" * num_dashes)


# Displays the word in lower case
def lower_case(word):
    print(word.lower())


# Displays the word in upper case
def upper_case(word):
    print(word.upper())


# Displays the word mirrored
def mirror_word(word):
    mirrored_word = ""
    for letter in reversed(word):
        mirrored_word += letter
    print(f"{word} | {mirrored_word}")


# Repeats the word
def repeat_word(word):
    print("How many times to repeat the word?")
    amount = int(input())

    # Finds out if the number is odd or even
    for i in range(amount):
        if i % 2 == 0:
            print(lower_case(word))
        else:
            print(upper_case(word))


# Runs
def run():
    print("Please enter a word:")
    word = input()

    # get the user's selection
    print("What would you like to do with this word?")
    print("[1] Display in a box")
    print("[2] Display lower-case")
    print("[3] Display upper-case")
    print("[4] Display mirrored")
    print("[5] Display repeated")
    print("[6] Quit")

    option = int(input())

    # Selects the correct function
    if option == 1:
        display_word_box(word)
    elif option == 2:
        lower_case(word)
    elif option == 3:
        upper_case(word)
    elif option == 4:
        mirror_word(word)
    elif option == 5:
        repeat_word(word)
    elif option == 6:
        print("Closing")
    else:
        print("Option not found")


run()


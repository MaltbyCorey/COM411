print("Program started")

# Gets a standard character from the user
print("Please enter a standard character:")
character = input()

if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("A single character was expected.")

print("Program ended")

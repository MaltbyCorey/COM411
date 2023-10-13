# Gets phrase from user
print("What phrase would you like to reverse?")
phrase = input()

# Loops for each letter in phrase
for position in range(len(phrase) - 1, -1, -1,):
    print(phrase[position], end="")

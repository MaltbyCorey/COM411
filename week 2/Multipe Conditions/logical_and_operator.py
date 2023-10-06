# Asks the user what was heard
print("What did I hear?")
noise = input()

# Asks the user what was seen
print("What did I see")
seen = input()

if noise == "grr" and seen == "two red eyes":
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")

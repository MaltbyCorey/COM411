# Asks the user what type of adventure
print("What type of adventure should I have?")
adventure_type = input()

# Branches based on input
if adventure_type == "scary" or adventure_type == "short":
    # Scary or short story
    print("Entering the dark forest!")
elif adventure_type == "safe" or adventure_type == "long":
    # Safe or long story
    print("Taking the safe route!")
else:
    # No route
    print("Not sure which route to take.")

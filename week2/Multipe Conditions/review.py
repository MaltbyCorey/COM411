# Asks the user where they are
print("Where are you?")
location = input()

# Branches based on location
if location == "City" or location == "Town":
    # Asks the user what the weather is like
    print("What is the weather like?")
    weather = input()

    # Branches based on weather
    if weather == "sunny":
        # Sunny day
        print("It's a sunny day in the park")
    else:
        # Rainy day
        print("It is to rainy to go in the park")

elif location == "Lost":
    # User is lost
    # Asks user what they can see
    print("What can you see?")
    seen_1 = input()
    print("What else can you see?")
    seen_2 = input()

    # Branches base on what can be seen
    if seen_1 == "trees" and seen_2 == "grass":
        # User is in the forest
        print("You are in the forest")
    else:
        # User is lost
        print("You are lost")
else:
    # User is lost
    print("You are lost")

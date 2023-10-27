"""
# Asks the user what book type they have
print("What type of cover does the book have?")
book_cover = input("")

# Branchs depending on input
if book_cover == "soft":
    # Asks the user if the book is perfect-bound
    print("Is the book perfect-bound?")
    answer = input("").lower()

    # Branchs based on input
    if answer == "yes":
        # Book is perfect bound
        print("Soft cover, perfect bound books are very popular!")
    else:
        # Book is not perfect bound
        print("Soft covers with coils or stitches are great for short books")
elif book_cover == "hard":
    print("Books with hard covers can be more expensive!")
"""

# Asks the user where to look
print("Where should I look?")
look = input("")

# Branches based on input
if look == "bedroom":
    # Looking in bedroom
    print("Where in the bedroom should I look?")
    bedroom_look = input("")

    if bedroom_look == "bed" :
        # Looking under the bed
        print("Found some shoes but no phone")
    else:
        # Looking somewhere else
        print("Found some mess but no phone.")

elif look == "bathroom":
    # Looking in the bathroom
    print("Where in the bathroom should I look?")
    bathroom_look = input()

    if bathroom_look == "bath":
        # Looking in the bath
        print("Found a rubber duck but no phone")
    else:
        # Looking somewhere else
        print("Found bathroom stuff but no phone.")

elif look == "living room":
    # Looking in living room
    print("Where in the living room should I look?")
    living_room_look = input()

    if living_room_look == "table":
        # Looking on the table
        print("Yes! I found my phone!")
    else:
        # Looking somewhere else
        print("Found some stuff but no phone.")
else:
    # Cannot find
    print("I do not know where that is but I will keep looking.")


"""
# Asks user about the type of book and gets their input
print("What type of book is this?")
book_type = input()

# If the book is adventure branch
if book_type == "adventure":
    print("I like adventure books!")

# Output final message
print("Finished reading book")

# Asks user about the activity being performed and gets input
print("Please enter the activity to be performed")
activity = input()

# Sets the input to lowercase
activity = activity.lower()

# Branches depending on the users input
if activity == "calculate":
    print("Perform calculation...")
else:
    print("Performing activity...")

# Outputs final message to user
print("Activity completed!")
"""

# Asks user for a direction
print("Towards which direction should I go (up, down, left or right)?")
direction = input()

# Branches depending on direction
if direction == "up":
    print("I am moving in an upward direction!")
elif direction == "down":
    print("I am moving in a downward direction!")
elif direction == "right":
    print("I am moving in a right direction!")
elif direction == "left":
    print("I am moving in a left direction!")
else:
    print("That is not a valid direction!")

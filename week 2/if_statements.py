"""
# Asks user about the type of book and gets their input
print("What type of book is this?")
book_type = input()

# If the book is adventure branch
if book_type == "adventure":
    print("I like adventure books!")

# Output final message
print("Finished reading book")
"""

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



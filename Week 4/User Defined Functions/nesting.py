# Identify function
def identify():
    # Ask user for what lies ahead
    print("What lies before us?")
    response = input()

    # Displays message
    if response == "a large boulder":
        return "Time to run"
    else:
        return "We will be fine"


# Calls the identify function
print(identify())

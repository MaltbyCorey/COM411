# Listen function
def listen():
    # Asks the user what sound they heard
    print("What sound did you hear?")
    sound = input()

    # Display message
    return f"That was a loud {sound}!"


# Calls the function
print(listen())

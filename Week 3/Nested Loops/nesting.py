# Gets a sequence from the user
print("Please enter a sequence")
sequence = input()

# Gets the marker from the user
print("Please enter the character for the marker")
marker = input()
marker1 = -1
marker2 = -1

# Loops for the amount of characters in string
for position in range(0, len(sequence), 1):
    letter = sequence[position]

    # If the letter is equal to marker
    if letter == marker:
        # If marker 1 is -1
        if marker1 == -1:
            # Add the position to marker1
            marker1 = position
        # Else add the position to marker2
        else:
            marker2 = position

# Output the distance to user
print(f"The distance between the marker is {marker2 - marker1 -1}")

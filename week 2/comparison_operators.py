# Asks the user for the first number
print("Please enter the first number")
first_number = int(input())

# Asks the user for the second number
print("Please enter the second number")
second_number = int(input())

# Branches based on input
if first_number > second_number:
    # First number is larger
    print("The first number is greater than the second number")
elif first_number < second_number:
    # Second number is larger
    print("The second number is greater than the first number")
else:
    # Both numbers are equal
    print("Both numbers are equal")

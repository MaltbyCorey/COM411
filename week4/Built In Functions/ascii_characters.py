print("Program started")

# Gets an ASCII code from the user
print("Please enter an ASCII code:")
ascii_code = int(input())

# Checks if the code entered is between 32 and 126
if 32 <= ascii_code <= 126:
    print(print(f"The character represented by the ASCII value {ascii_code} is: {chr(ascii_code)}"))
else:
    print("The character cannot be displayed.")

print("Program ended")
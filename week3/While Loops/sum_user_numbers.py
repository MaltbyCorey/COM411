print("How many numbers should I sum up?")
num = int(input())
total = 0

# Loops the amount of times the user has asked for
for count in range(num):
    # Gets number from user
    print(f"Please enter number {count + 1} of {num}")
    # Adds input to the total
    total += int(input())
# Prints total
print(f"The answer is {total}.")

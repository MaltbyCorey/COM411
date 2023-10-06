# Asks the user for the first number
print("Please enter the first whole number")
first_number = int(input())

# Asks the user for the second number
print("Please enter the second whole number")
second_number = int(input())

# Asks the user for the third number
print("Please enter the third whole number")
third_number = int(input())

# Adds number to array
numbers = [first_number, second_number, third_number]

# Starts the counter
even = 0
odd = 0
n = 0

while n < 3:
    if numbers[n] % 2 == 0:
        even += 1
    else:
        odd += 1
    n += 1

print(f"There where {even} even and {odd} odd numbers")





# Ask user to enter their name
print("What is your name?")
name = input()

print("What is your age?")
age = int(input())

print("What is your weight?")
weight = float(input())

print("What is your height?")
height = float(input())

# Calculate bmi
bmi = round(weight / (height ** 2), 2)

# Display result
print(f"{name} your bmi is {bmi}")

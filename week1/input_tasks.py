# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

# Display a box
print("##########")
print("# 0    0 #")
print("#   __   #")
print("##########")

age = input("How old are you (in years)?")
height = input("How tall are you (in meters)?")
weight = input("How much do you weigh (in kilograms)?")
heightsquared = height * height
bmi = weight / heightsquared
print(f"{name} you are {age} years old and your bmi is {bmi}")
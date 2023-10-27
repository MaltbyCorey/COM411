# Importing modules
import random


# Checking guess function
def check_guess(rnd, mini, maxi):
    guess = int
    while guess != random_number:
        print(f"I am thinking of a number between {mini} and {maxi}.  Can you guess what it is?")
        guess = int(input())
        if guess < rnd:
            print("To low")
            print("Try again")
        elif guess > rnd:
            print("To high")
            print("Try again")

    print("Correct!")


# Gets a min and max value from the user
print("Please enter the minimum value")
min_value = int(input())
print("Please enter the maximum value")
max_value = int(input())

# Generates a random number between the min and max value
random_number = random.randrange(min_value, max_value)

check_guess(random_number,min_value, max_value)

import random
import os
from math import log, ceil


print("Welcome to the Number Guessing Game!")
print("Please, insert the lower limit of the range")

lower_limit_positive = False
while not lower_limit_positive:
    while True:
        try:
            lower_limit = int(input("Lower limit: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    if lower_limit < 0:
        print("The lower limit cannot be negative.")
    else:
        lower_limit_positive = True

print("Please, insert the upper limit of the range")
upper_limit_positive = False
while not upper_limit_positive:
    while True:
        try:
            upper_limit = int(input("Upper limit: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    if upper_limit < 0 or upper_limit <= lower_limit:
        print(f"The upper limit must be positive and greater than {lower_limit}!")
    else:
        upper_limit_positive = True



random_number = random.randint(lower_limit, upper_limit)
chances = ceil(log(upper_limit - lower_limit + 1) / log(2))
os.system('cls' if os.name == 'nt' else 'clear')
print("The game will start now!")
print(f"You have {chances} attempts")

attempts = 0


def print_chances():
    print(f"You have {chances - attempts} chances left!")

while attempts < chances:

    print("Please, insert your guess: ")
    try:
        user_guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    attempts += 1

    
    if user_guess < lower_limit or user_guess > upper_limit:
        print("Remember the limits!")
        print(f"The number is between {lower_limit} and {upper_limit}")
        print("Try again!")
        print_chances()
    elif random_number < user_guess:
        print("Try lower!")
        print_chances()
    elif random_number > user_guess:
        print("Try higher!")
        print_chances()
    else:
        print("You win")
        print(f"The random number was {random_number}")
        break
    
    if attempts == chances:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You lose")
        print(f"The random number was {random_number}")
        break

print("Game Over")
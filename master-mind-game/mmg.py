import random
import time
import os

random_number = random.randint(1000, 9999)
random_number = str(random_number)
#print(random_number)

print("Welcome to Master Mind Game!")
print("I have selected a 4-digit number 🤖")
print("Your task is to guess the number")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')


correct = ['X'] * 4
tries = 0

def print_correct_digits():
    print("***********")
    for k in correct:
        print(k, end=' ')
    print("\n*********")


while True:
    
    print_correct_digits()
    print("Now enter your guess (or 'z' to give up)")
    guess = input("Enter your guess: ").strip()

    if guess.lower() == 'z':
        print(f"The number was {random_number}")
        break

    if len(guess) != 4 or not guess.isdigit():
        print("Please enter a valid 4-digit number.")
        continue

    tries += 1

    if guess == random_number:
        print(f"Congratulations! 🎉")
        print(f"You win!")
        print(f"You took {tries} tries to guess the number.")
        break

    valid_digits = 0
    for i in range(0, 4):
        if guess[i] == random_number[i]:
            correct[i] = guess[i]
            valid_digits += 1
        
    if valid_digits != 0:
        print(f"It is not correct but you have {valid_digits} valid digits correct")
    else:
        print("No valid digits correct. Try again!")

print("GAME OVER")
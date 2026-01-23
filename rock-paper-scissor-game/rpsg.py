import time
import random
import os
print("Welcome to the Rock-Paper-Scissor Game!")
time.sleep(2)


name = input("Enter your name: ")

choices = {1: 'Rock 🪨', 2: 'Paper 📄', 3: 'Scissor ✂️'}


def get_computer_choice():
    return choices[random.randint(1, 3)]



while True:
    
    computer_choice = get_computer_choice()
    
    while True:
        print("Choose your option:")
        print("1. Rock 🪨")
        print("2. Paper 📄")
        print("3. Scissor ✂️")
        user_input = int(input("Enter the number: "))
        if user_input < 1 or user_input > 3:
            print("Invalid input. Please enter a number between 1 and 3.")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            break
        
    user_choice = choices[user_input]

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{name:<10}: {user_choice}")
    print(" " * 5 + "VS")
    print(f"{'Computer':<10}: {computer_choice}")
    time.sleep(2)
    

    if user_choice == computer_choice:
        print("It's a tie!")
        print("Let's play again...")
        time.sleep(1)
        continue
    else:
        wins = {'Rock 🪨': 'Scissor ✂️', 
                'Paper 📄': 'Rock 🪨',
                'Scissor ✂️': 'Paper 📄'}
        
    if wins[user_choice] == computer_choice:
        print(f"{name} wins! 🎉")
        break
    else:
        print("Computer wins! 🤖")
        break

print("GAME OVER")



import random
import time

current_number = 0
print("Welcome to the 21 Number Game!")
name = input("Plase enter your name: ")

def computer_moves():
    global current_number
    computer_intents = random.randint(1, 3)
    while computer_intents > 0:
        current_number += 1
        print(f"Computers says: {current_number}")
        check_winner()
        if game_over:
            break
        computer_intents -= 1
        time.sleep(1)

def player_moves():
    global current_number
    while True:
        user_input = input("How many numbers will you say (1-3)? ")
        try:
            player_intents = int(user_input)
            if player_intents < 1 or player_intents > 3:
                print("Invalid input. Choose between 1 and 3.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
    while player_intents > 0:
        current_number += 1
        print(f"{name} says: {current_number}")
        check_winner()
        if game_over:
            break
        player_intents -= 1
        time.sleep(1)

def check_winner():
    global game_over
    if current_number >= 21:
        game_over = True
        if turn == "computer":
            print(f"{name} wins!")
        else:
            print("Computer wins! 🤖")

turn = random.choice(["computer", "player"])
game_over = False

while not game_over:
    if turn == "computer":
        print("\nComputer's turn...")
        computer_moves()
        if not game_over:
            turn = "player"
    else:
        print(f"\n{name}'s turn...")
        player_moves()
        if not game_over:
            turn = "computer"



import random
import os 
import time


#WELCOME
name = input("Hello, what is your name: ")
print(f"Hello {name}, and good luck!")
print("The word is a programming language")
time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")

#RANDOM WORD
words = ['python', 'java', 'kotlin', 'javascript', 'go', 'c', 'c++', 'swift']
random_word = random.choice(words)

attempts = 15
guesses = ''

while attempts > 0:

    words_to_discover = 0

    #print the hints or the correct chars
    for char in random_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            words_to_discover += 1
    
    #Winning case
    #No words to discover

    if words_to_discover == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n YOU WIN!")
        print(f"THE WORD IS '{random_word}'")
        break
    print()

    while True:
        print(f"You have {attempts} attempts left")
        guess = input("Guess a character: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Insert a one valid character")
            continue
        break

    guesses += guess


    if guess not in random_word:
        attempts -= 1
        print("Wrong")
        print(f"You have {attempts} attempts left ")

    if attempts == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("GAME OVER ❌")
        print("You lose")
        print(f"The word was '{random_word}'")

from art import logo 
from art import win
from art import gameOver
import random
import os

def clear():
  os.system('clear')


number = random.randint(1,100)
lives = 0



print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficult == "easy":
    lives = 10
    print("You have 10 attemps")
else:
  lives = 5
  print("You have 5 attemps")


end_of_game = False

while not end_of_game:
  
  guess = int(input("Make a guess: "))
  clear()
  if guess == number:
    print(win)
    end_of_game = True
  elif guess < number:
    print("Guess to low")
    lives -= 1
  elif guess > number:
    print("Guess to high")
    lives -= 1
    
  if lives == 0:
    clear()
    print(gameOver)
    print("0 ATTEMPS LEFT")
    print(f"THE NUMBER WAS: {number}")
    break 

  print(f"\nAttemps left: {lives}\n")
  
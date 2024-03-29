import random
import hangman_art
import hangman_words
import os

def clear():
     os.system('clear')


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)


#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guess_words = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    guess_words.append(guess)
    
    clear()

    print("-------------------------")
    print("WORDS ALREADY GUESS")
    print(guess_words)
    print("------------------------- \n")

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"{guess} already guessed")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
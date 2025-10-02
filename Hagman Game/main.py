import hangmanArt
import words
import random

def print_hangman(mistakes):
    for line in hangmanArt.hangman_art[mistakes]:
        print(line)

def print_hints(guess):
    for i in range(len(choice)):
            if choice[i] == guess:
                hints[i] = guess
    print()
    print(hints)


mistakes = 0
game_over = False
choice = random.choice(words.words).lower()
hints = ['_'] * len(choice)


if __name__ == '__main__':

    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    print("BIENVENIDO A SOCCER-HANGMAN ⚽")
    print("ADIVINA EL JUGADOR SECRETO  🔐")
    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")

    #Game Init
    while not game_over:
        
        if not "_" in hints:
            print("🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆")
            print("\033[92mHAZ GANADO!\033[0m 🏆")
            print("🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆")
            game_over = True
            continue
        
        if mistakes == 6:
            print("\033[91mGAME OVER\033[0m 😵")
            print(f"EL JUGADOR SECRETO ERA: \033[94m{choice.capitalize()}\033[0m")
            game_over = True
            continue
        
        
        guess = input("\nIngresa una letra: ").lower()

        #Validaciones y salir del juego prematuro
        if guess == "exit":
            game_over = True
        elif guess == "":
            print("Tienes que ingresar una letra")
        elif len(guess) > 1:
            print("Tiene que ser solo 1 letra")
        elif guess.isdigit():
            print("Tiene que ser una letra, no un numero")
        elif guess not in choice:
            mistakes += 1
            print(f"Mistakes = {mistakes} \n")
        

        print_hangman(mistakes)
        print_hints(guess)

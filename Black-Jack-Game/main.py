
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


import random
from art import logo
import os

def clear():
     os.system('clear')

def checkAce(cards, total):
    if ace in cards and total > 21:
        total -= 10
        return True


ace = 11
playing = True
while playing:

    choose = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    clear()

    if choose == "n":
        playing = False
    else:
        print(logo)
        userCards = []
        totalUser = 0
        for i in range(2):
            card = random.choice(cards)
            userCards.append(card)
            totalUser += card
            if checkAce(userCards, totalUser):
                print("Ace of USER convert to 1 to not go out of 21!")
        print(f"{userCards} = Total of user cards: {totalUser} ")

        computerCards = []
        totalComputer = 0
        computerCard = random.choice(cards)
        computerCards.append(computerCard)
        totalComputer = computerCard

        print(f"{computerCards} = Total of computer Cards: {totalComputer}")

        if totalUser <= 20:
            anotherCard = input(
                "Type 'y' to get another card, type 'n' to pass:")
            if anotherCard == "y":
                card = random.choice(cards)
                userCards.append(card)
                totalUser += card
                if checkAce(userCards, totalUser):
                    totalUser -= 10
                    print("Ace USER convert to 1 to not go out of 21!")

        while totalComputer < 21:
            nextComputerCard = random.choice(cards)
            computerCards.append(nextComputerCard)
            totalComputer += nextComputerCard

        print(f"{userCards} = Total of user cards: {totalUser} ")
        print(f"{computerCards} = Total of computer Cards: {totalComputer}")

        if totalUser > 21:
            print("Total out of 21. You Lose!")
        elif totalComputer > 21:
            print("Computer out of 21. You win!")
        elif totalUser == totalComputer:
            print("TIE")
        elif totalUser > totalComputer:
            print("You win!")
        else:
            print("Computer wins!")


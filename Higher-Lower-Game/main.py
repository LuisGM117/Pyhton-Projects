import random
from art import logo
from art import vs
from game_data import data
import os

def clear():
    os.system('clear')


def randomPerson(data):
    random_number = random.randint(0, len(data) - 1)
    person_dictionarie = data[random_number]
    return person_dictionarie


def printPerson(dictionarie):
    person = ""
    for key in dictionarie:
        if key != "follower_count":
            person += str(dictionarie[key]) + ", "
    person = person[:-2] + "." 
    return person


person1 = randomPerson(data)
person2 = randomPerson(data)


def against(p1, p2, hits):
    clear()
    print(logo)

    print(f"A: {printPerson(p1)}")
    print(vs)
    print(f"B: {printPerson(p2)}")

    choose = input("\nWho has more followers? Type 'A' or 'B': \n")

    if choose == "A":
        if p1["follower_count"] > p2["follower_count"]:
            hits = hits + 1
            nextPerson = randomPerson(data)
            against(p1, nextPerson, hits)
        else:
            print(f"\nYou Lose. Total hits: {hits}\n")
    elif choose == "B":
        if p2["follower_count"] > p1["follower_count"]:
            hits += 1
            nextPerson = randomPerson(data)
            against(p2, nextPerson, hits)
        else:
            print(f"\nYou Lose. Total hits: {hits}\n")


hits = 0
against(person1, person2, hits)

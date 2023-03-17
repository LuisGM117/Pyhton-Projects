#Simple but powerful password generator

import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

list = []
for i in range(0, 4):
    list.append(random.choice(letters))

for i in range(0, 4):
    list.append(random.choice(numbers))

for i in range(0, 4):
    list.append(random.choice(symbols))


random.shuffle(list)


password = ""
for char in list:
    password += char
print(password)
pyperclip.copy(password)

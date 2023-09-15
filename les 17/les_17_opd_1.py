import random
from termcolor import colored

getal1 = random.randint (1, 5)

raadgetal = int(input("raad een getal tussen 1 en 5 "))

if getal1 == raadgetal:
    print(colored("goed geraden", "green"))
else:
    print(colored("verkeerd geraden!", "red"))
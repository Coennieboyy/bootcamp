import random
from termcolor import colored

getal1 = random.randint(1,5)
getal_invullen = True
kansen = 2

while getal_invullen:
    try:
        raadgetal = int(input("raad een getal tussen 1 en 5 "))
    except ValueError:
        print("vul een getal in tussen 1 en 5! ")

    if raadgetal == getal1:
        print(colored("goed geraden", "green"))
        getal_invullen = False

    elif kansen == 0:
        getal_invullen = False

    else:
        kansen -= 1
        print(colored("verkeerd geraden!", "red"))
        getal_invullen = True
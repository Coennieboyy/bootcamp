import random
from termcolor import colored

getal1 = random.randint(1,5)
getal_invullen = True
kansen = 3
Jalist = ["ja", "j", "y", "yes"]
rondes = 1
fouten = 0

while getal_invullen:
    try:
        raadgetal = int(input("raad een getal tussen 1 en 5 "))
    except ValueError:
        print("vul een getal in tussen 1 en 5! ")

    if raadgetal == getal1:
        print(colored(f"goed geraden", "green"))
        vraag = input("wil je nog potje spelen j/n ").lower()
        rondes += 1
        if vraag in Jalist:
            getal1 = random.randint(1, 5)
            print("Suc6")
            kansen = 3
        else:
            print("Tot ziens")
            getal_invullen = False

    elif kansen >= 1:
        kansen -= 1
        fouten += 1
        print(colored("verkeerd geraden!", "red"))
        getal_invullen = True
    
    if kansen == 0:   
        vraag = input("wil je nog potje spelen j/n ")
        if vraag in Jalist:
            getal1 = random.randint(1, 5)
            print("Suc6")
            kansen = 3
        else:
            print("Tot ziens")
            getal_invullen = False

    
print(f"je hebt {rondes} rondes gespeeld en {fouten} fouten gemaakt ")
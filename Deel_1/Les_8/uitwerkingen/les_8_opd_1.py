cijfer = int(input("kies een cijfer tussen 1 t/m 10? ")) 

if cijfer == 1:
    omschrijving = ("zeer slecht")

elif cijfer == 2:
    omschrijving = ("slecht")

elif cijfer == 3:
    omschrijving = ("gering")

elif cijfer == 4:
    omschrijving = ("onvoldoende")

elif cijfer == 5:
    omschrijving = ("bijna voldoende")

elif cijfer == 6:
    omschrijving = ("voldoende")

elif cijfer == 7:
    omschrijving = ("ruim voldoende")

elif cijfer == 8:
    omschrijving = ("goed")

elif cijfer == 9:
    omschrijving = ("zeer goed")

elif cijfer == 10:
    omschrijving = ("uitmuntend")

elif cijfer >= 6:
    omschrijving = ("gefeliciteerd")

else:
    print("dit kan ik niet omzetten! ")

if cijfer >= 6 and cijfer <= 10:
    print(f"gefeliciteerd, {omschrijving} je resultaat is een {cijfer}")

elif cijfer < 6 and cijfer >= 1:
    print(f"jammer, {omschrijving} je resultaat is een {cijfer}")





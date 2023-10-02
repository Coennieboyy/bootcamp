#opdracht 1
#a: omdat bij visualstudio code extensions kan toevoegen en j ecode is duidelijk te zien met kleurtjes
#b: omdat als je het niet pushed zie je dat als nog niet staan bij github.com

#opdracht 2
# Maak het commentaar af.
a = 5  # dit is een voorbeeld van het datatype: int
b = 10.5# dit is een voorbeeld van het datatype: float
c = "Hallo wereld" # dit is een voorbeeld van het datatype: string

#odpracht 3
# Schrijf code die de waarden van a en b omwisselt. Gebruik daarvoor een extra variabele.
a = 5
b = 10
c = 5
a = a + c
b = b - c
# voeg jouw code toe…
# Controleer met onderstaande code of de waarden correct zijn verwisseld
print(f"a = {a}, b = {b}") # Moet "a = 10 b = 5" printen

#odpracht 4
# Los de problemen op (zonder exception handling).
leeftijd = int(input("Hoe oud ben je? "))
print(f"Dan duurt het nog ongeveer {67 - leeftijd} jaar voordat je met pensioen mag!")
# Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!

#odpracht 5
# Schrijf een functie die 3 getallen bij elkaar optelt en zorg ervoor
# dat de uitkomst ervan wordt getoond in de print
getal1 = 200
getal2 = 5
getal3 = 12

def som(getal1, getal2, getal3):
    Som = getal1 + getal2 + getal3
    return Som

antwoord = som(getal1, getal2, getal3) # of de naam van je eigen functie.
print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")

#opdracht 6
# Maak de volgende code af:# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.
AANTAL_GB = 20 # Aantal GB data in je bundel
AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
ONBEPERKT = True # test ook met True
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
if (aantal_minuten_gebeld > AANTAL_MINUTEN and ONBEPERKT == False) or (aantal_GB_internet > AANTAL_GB and ONBEPERKT == False):
    print("Let op: je moet bijbetalen!")
else:
    print("Niet aan de hand gebruik je mobiel lekker verder!")

#odpracht 7
# Print onder elkaar de getallen 1-250 met max 2 regels code.
for i in range(251):
    print(i)
    
#Opdracht 8
# Gegeven is:

lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']


# a: print een eenvoudig menu met de volgende layout:

print("onze menukaart:")
print("appel")
print("pannenkoek")
print("kiwi")
print("hamburger")

# b: Schrijf code die ervoor zorgt dat alleen het eten met de langste naam wordt geprint in de terminal. # Let op: je moet in de code eerst bepalen welk eten de langste naam heeft (en dus niet hardcoded 1 voor de index gebruiken). # test je code door extra eten toe te voegen met een nog langere naam.
maxlen = -1
for length in lijst_eten:
    if len(length) > maxlen:
        maxlen = len(length)
        woord = length
 
print(f"langste naam van het eten is {woord}")

#Opdracht 9
# Schrijf een programma wat de gebruiker vraagt een cijfer in te voeren via de terminal.
# Dit blijf je herhalen totdat de gebruiker een getal tussen 0 en 10 heeft ingevoerd.
# Voert de gebruiker iets anders in dan een getal: geef een foutmelding.
getal_invullen = True

while getal_invullen:                                                                 
        try:                                                                        
            getal = int(input("Vul een getal in: "))
            if getal > 10:
             raise ValueError        
        except ValueError:                                                          
            print("vul een getal in tussen 0 en 10!")
        if getal < 10:                                                     
            print(f"goed geraden!")
            break

#Opdracht 10:
# repareer de volgende code:
MAX = 20
getal = int(input("Voer een getal in "))
if getal > MAX:
   input(f"Het getal is groter dan {MAX}")
elif getal < MAX:
  input(f"Het getal is kleiner dan {MAX}")
else:
   input(f"Het getal is gelijk aan {MAX}")

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
def rekensom(som):
    som = getal1 + getal2 + getal3
    

getal1 = 200
getal2 = 5
getal3 = 12
antwoord = rekensom() # of de naam van je eigen functie.
print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")
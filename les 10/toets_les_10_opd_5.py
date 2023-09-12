from time import sleep # je hoeft nog niet te weten wat een import is, Kopieer deze regel en je kunt je programma laten wachten met de opdracht sleep(x seconden)


oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig? '))
prijs_m2 = 40

# print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
# sleep(1)
# print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
# sleep(1)
# print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
# sleep(1)

# secret code containing the answer of question 2
for i in range(5):
    sleep(1)
    print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")

# end of secret

totaal = prijs_m2 * oppervlakte

print(f'Het scherpste prijs voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))
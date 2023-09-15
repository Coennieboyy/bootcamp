leeftijd = int(input("voer een leeftijd in onder of boven de 18? "))
snor = input("heb je een snor j/n? ") 
diploma = input("heb je een diploma j/n? ")

if leeftijd >= 18 and snor == "j" or leeftijd < 18 and diploma == "j":
    print("gefeliciteerd je bent aangenomen.")
else:
    print("sorry je bent helaas niet aangenomen")
naam = input("voer je naam in. ")
leeftijd = int(input("voer je leeftijd in jaren in. "))

if leeftijd >= 18:
    print(f"beste {naam} je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans). ")
else:
    print(f"beste {naam} je bent nog geen 18. Alleen autorijden zit er dus niet in :-( ")
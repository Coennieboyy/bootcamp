naamlijst = ["aviel" , "zedrick" , "jacco" , "tim" , "coen"]
naam = input("voer een naam in. ")

if naam in naamlijst:
    naamlijst.remove(naam)
    print(naamlijst)
else:
    naamlijst.append(naam)
    print(naamlijst)
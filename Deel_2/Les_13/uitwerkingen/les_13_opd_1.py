mytuple = tuple (("rood" , "geel" , "blauw" , "groen" , "paars"))

naam = input("hoe heet je? ")
kleur = input("wat is je favoriete kleur ")

if kleur in mytuple:
    print(f"{kleur} is een mooie kleur {naam}. " )

else:
    ("deze kleur is niet geweldig")
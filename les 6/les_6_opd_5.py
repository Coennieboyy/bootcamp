a = int(input("voer cijfer in "))
b = int(input("voer cijfer in "))
c = int(input("voer cijfer in "))


if (a > b) and (a > c):
  print("Variabele a is het grootst want" , a ,  "is groter dan" , b , "en groter dan" , c , )

elif (b > a) and (b > c):
  print("Variabele b is het grootst want" , b , "is groter dan" , a , "en groter dan" , c , )

elif (a == b) and (b == c):
  print("alles is gelijk")

else:
  print("Variabele c is echt grootst") 
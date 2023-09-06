i = 10000
rente = 2.8
jaar = 0

while jaar < 15:
    jaar += 1

    i += i / 100 * rente
    print(f"na {jaar} heb je {round(i)} op je rekenining staan")

#na 5 jaar heb je 11481
#na 15 jaar heb je 15132




    

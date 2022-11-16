# Savoir si un nombre est premier
while True:
    nb = int(input(">> "))
    liste = []
    if nb == 0:
        print("Pas premier")
        continue

    for i in range(1, nb + 1):
        if nb % i == 0:
            liste.append(i)
        


    if len(liste) > 2:
        print("Pas premier")
    else:
        print("Premier")
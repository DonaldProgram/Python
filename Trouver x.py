# test trouver x 
while True:
    print("")
    Choix = str(input("+ ou - >> "))
    NBx = int(input("Nombre de x >> "))
    NB = int(input("Nombre chiffre >> "))
    ResultatDonnée = int(input("Resultat >> "))
    if Choix == "-":
        Resultat = ResultatDonnée + NB
    elif Choix == "+":
        Resultat = ResultatDonnée - NB


    Reductions = []

    for a in range(1, Resultat + 1):
        if Resultat % a == 0 and NBx % a == 0:
            Reductions.append(a)

    print(Resultat / max(Reductions))
    print(NBx / max(Reductions))
    
# le jeu du casino 1

import time
import random

Cagnotte = 10


a = True

while a:
    Choix = input("p : prudent ou r : risque >> ")

    if Choix == 'p':
        print('')
        print('Choix prudent')
        DèsListe = [1, 2, 3, 4, 5, 6]
        Dès = random.choices(DèsListe)
        print("Tu as fait", Dès[0])
        if Dès[0] <= 4:
            Cagnotte += 2
            print("Cagnotte :",Cagnotte)
        else:
            Cagnotte -= 1
            print("Cagnotte :",Cagnotte)

    elif Choix == 'r':
        print('')
        print("Choix risque")
        DèsListe = [1, 2, 3, 4, 5, 6]
        Dès = random.choices(DèsListe)
        print("Tu as fait", Dès[0])
        if Dès[0] >= 5:
            Cagnotte += 7
            print("Cagnotte :",Cagnotte)
        else:
            Cagnotte -= 3
            print("Cagnotte :",Cagnotte)

    if Cagnotte >= 20 or Cagnotte <= 0:
        a = False

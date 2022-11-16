import random
import time

ChoixNBplayer = int(input("1 joueur ou deux joueurs : "))

ListeNombreDès = [1, 2, 3, 4, 5, 6]
Cagnotte = 10
Cagnotte2 = 10
a = True
while a:
    if ChoixNBplayer == 1:
        print('')
        Dès = random.choices(ListeNombreDès)
        time.sleep(2)
        print("Tu as fait",Dès[0])
        
        if Dès[0] >= 5:
            Cagnotte += 3
            print("Cagnotte :",Cagnotte,"€")
        else:
            Cagnotte -= 2
            print("Cagnotte :",Cagnotte,"€")

        if Cagnotte <= 0 or Cagnotte >= 20:
            a = False

    elif ChoixNBplayer == 2:
        print('')
        Dès = random.choices(ListeNombreDès)
        time.sleep(2)
        print("Joueur RDE a fait",Dès[0])
        print("Cagnotte RDE :", Cagnotte,"€")
        print('')
        print('')
        Dès = random.choices(ListeNombreDès)
        time.sleep(2)
        print("Joueur GM1 a fait :",Dès[0])
        print("Cagnotte GM1 :",Cagnotte2,"€")

        if Cagnotte <= 0 or Cagnotte >= 20 or Cagnotte2 <= 0 or Cagnotte2 >= 20 :
            a = False
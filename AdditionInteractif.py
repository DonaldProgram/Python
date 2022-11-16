# Addition Interactif
import random

class Couleur:
    Vert= '\033[92m' 
    Bleu = '\033[94m' 
    Rouge = '\033[91m' 
    Normal = '\033[0m' 
while True:
    print("")
    print("")
    liste1 = [1, 2, 3]
    NBrandom1 = random.choice(liste1)

    liste2 = [1, 2, 3, 4, 5, 6]
    NBrandom2 = random.choice(liste2)


    print(Couleur.Vert + " |",NBrandom1,"|")
    print("+|",NBrandom2,"|" + Couleur.Normal)
    print("-------")

    Reponse = int(input("Reponse >> "))

    print(Couleur.Vert + " |",NBrandom1,"|")
    print("+|",NBrandom2,"|" + Couleur.Normal)
    print("-------")

    if Reponse == (NBrandom1 + NBrandom2):
        print(Couleur.Vert," ", Reponse, Couleur.Normal)
    else:
        print(Couleur.Rouge," ", Reponse, Couleur.Normal)
        while Reponse != (NBrandom1 + NBrandom2):
            print("")
            Reponse = int(input("Reponse >> "))
            
            if Reponse != (NBrandom1 + NBrandom2):
                print("")
                print("")
                print(Couleur.Vert + " |",NBrandom1,"|")
                print("+|",NBrandom2,"|" + Couleur.Normal)
                print("-------")
                print(Couleur.Rouge," ", Reponse, Couleur.Normal)
            
            else:
                print("")
                print("")
                print(Couleur.Vert + " |",NBrandom1,"|")
                print("+|",NBrandom2,"|" + Couleur.Normal)
                print("-------")
                print(Couleur.Vert," ", Reponse, Couleur.Normal)

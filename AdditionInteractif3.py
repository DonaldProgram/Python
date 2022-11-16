import random

class Couleur:
    Vert= '\033[92m' 
    Bleu = '\033[94m' 
    Rouge = '\033[91m' 
    Normal = '\033[0m' 

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

NB1 = random.choice(liste)
NB2 = random.choice(liste)
NB3 = random.choice(liste)
NB4 = random.choice(liste)

print(Couleur.Rouge +" |?| |?|")
print(Couleur.Bleu + "    |",NB3, "||",NB1,"|")
print("+   |",NB4,"||",NB2,"|")
print("   ------------" + Couleur.Normal)
print(Couleur.Rouge + "     |?|  |?|" + Couleur.Normal)

AdditionREPC1 = NB1 + NB2
if AdditionREPC1 > 9:
    AdditionREPC1 -= 10
    retenue = 1
else:
    retenue = 0

print('')
AdditionC1 = int(input("Colonne1 >> "))

if AdditionC1 == AdditionREPC1:
    print(Couleur.Rouge +" |?| |?|")
    print(Couleur.Bleu + "    |",NB3,"||",NB1,"|")
    print("+   |",NB4,"||",NB2,"|")
    print("   ------------" + Couleur.Normal)
    print(Couleur.Bleu + "     |?|  |",AdditionC1,"|" + Couleur.Normal)

else:
    print(Couleur.Rouge +" |?| |?|")
    print(Couleur.Bleu + "    |",NB3, "||",NB1,"|")
    print("+   |",NB4,"||",NB2,"|")
    print("   ------------" + Couleur.Normal)
    print(Couleur.Rouge + "     |?|  |",AdditionC1,"|" + Couleur.Normal)

Retenue = int(input("Retenue >> "))

print("")

if Retenue == retenue:
    print(Couleur.Bleu +"|?|",Couleur.Bleu,"|",Retenue,"|")
else:
    print(Couleur.Rouge + "|?| |",Retenue,"|")

print(Couleur.Bleu + "    |",NB3, "||",NB1,"|")
print("+   |",NB4,"||",NB2,"|")


if AdditionREPC1 == AdditionC1:
    print("   ------------" + Couleur.Normal)
    print(Couleur.Bleu + " |?||",AdditionC1,"|" + Couleur.Normal) 


else:
    print("------------" + Couleur.Normal)
    print(Couleur.Rouge + " |?||",AdditionC1,"|" + Couleur.Normal) 


AdditionREPC2 = retenue
AdditionC2 = int(input("Colonne 2 >> "))

print("")

if Retenue == retenue:
    print(Couleur.Bleu + " |",Retenue,"|")
else:
    print(Couleur.Rouge + " |",Retenue,"|")

print(Couleur.Bleu + " |",NB3, "||",NB1,"|")
print("+|",NB4,"||",NB2,"|")


if AdditionREPC1 == AdditionC1 and AdditionC2 == AdditionREPC2:
    print("------------" + Couleur.Normal)
    print(Couleur.Bleu + " |",AdditionC2,"||",AdditionC1,"|" + Couleur.Normal) 


else:
    print("------------" + Couleur.Normal)
    print(Couleur.Rouge + " |",AdditionREPC2,"||",AdditionC1,"|" + Couleur.Normal) 

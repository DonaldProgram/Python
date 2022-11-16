# Pour changer la couleur du texte
class Couleur:
    Vert= '\033[92m' 
    Bleu = '\033[94m' 
    Rouge = '\033[91m' 
    Normal = '\033[0m' 

NombreErreur = 0

print("  (2)  (1)")# pour reconnaitre les colonnes

print(Couleur.Bleu + " |___||___|" + Couleur.Normal)
print(Couleur.Bleu + "+|___||___|" + Couleur.Normal)
print(Couleur.Rouge + "  |_|" + Couleur.Normal)

print("")

colonne1H = int(input("Colonne 1 Haut >> "))

if colonne1H > 9:
    NombreErreur += 1

print("")

print("  (2)  (1)")
print(Couleur.Bleu + " |___||",colonne1H ,"|" + Couleur.Normal)
print(Couleur.Bleu + "+|___||___|" + Couleur.Normal)
print(Couleur.Rouge + "  |_|" + Couleur.Normal)


print("")

colonne1B = int(input("Colonne 1 Bas >> "))

if colonne1B > 9:
    NombreErreur += 1

print("  (2)  (1)")
print(Couleur.Bleu + " |___||",colonne1H,"|" + Couleur.Normal)
print(Couleur.Bleu + "+|___||",colonne1B,"|" + Couleur.Normal)
print(Couleur.Rouge + "  |_|" + Couleur.Normal)

print("")

colonne2H = int(input("Colonne 2 Haut >> "))

if colonne2H > 9:
    NombreErreur += 1

print("  (2)  (1)")
print(Couleur.Bleu + " |",colonne2H,"||",colonne1H ,"|" + Couleur.Normal)
print(Couleur.Bleu + "+|___||",colonne1B,"|" + Couleur.Normal)
print(Couleur.Rouge + "  |_|" + Couleur.Normal)

print("")

colonne2B = int(input("Colonne 2 Bas >> "))

if colonne2B > 9:
    NombreErreur += 1

print("  (2)  (1)")
print(Couleur.Bleu + " |",colonne2H,"||",colonne1H ,"|" + Couleur.Normal)
print(Couleur.Bleu + "+|",colonne2B,"||",colonne1B,"|" + Couleur.Normal)
print(Couleur.Rouge + " |_|" + Couleur.Normal)
print("")
Reste1 = 0
Reste2 = 0
NewCol3 = 0

if NombreErreur != 0:
    print("Il ne faut que 1 chiffre inferieur a 10 dans chaque colonne")

elif NombreErreur == 0:
    ResultatC1 = colonne1B + colonne1H

    if ResultatC1 > 9:
        Reste1 += 1
        ResultatC1 -= 10
    ResultatC2 = colonne2B + colonne2H + Reste1

    if ResultatC2 > 9:
        Reste2 += 1
        ResultatC2 -= 10
        NewCol3 = 1

if NewCol3 == 0:
    print("    (2)  (1)")
    print(Couleur.Bleu + "   |",colonne2H,"||",colonne1H ,"|" + Couleur.Normal)
    print(Couleur.Bleu + "+  |",colonne2B,"||",colonne1B,"|" + Couleur.Normal)
    print(Couleur.Rouge + "   |",Reste1,"|" + Couleur.Normal)
    print(Couleur.Vert + "   |",ResultatC2,"||",ResultatC1,"|" + Couleur.Normal)

    print("")

elif NewCol3 == 1:
    print("      (2)  (1)")
    print(Couleur.Bleu + "     |",colonne2H,"||",colonne1H ,"|" + Couleur.Normal)
    print(Couleur.Bleu + "  +  |",colonne2B,"||",colonne1B,"|" + Couleur.Normal)
    print(Couleur.Rouge + "|",Reste2,"||",Reste1,"|" + Couleur.Normal)
    print(Couleur.Vert +"|",Reste2,"||",ResultatC2,"||",ResultatC1,"|" + Couleur.Normal)

    print("")
print("$_$")

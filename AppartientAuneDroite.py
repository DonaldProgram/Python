import random
ReponseDemande = None

ListeChiffres = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("f(x) = ax + b")

ax = random.choice(ListeChiffres)
b = random.choice(ListeChiffres)
print("f(x) = " + str(ax) + "x +(" + str(b) + ")")

PointAa = random.choice(ListeChiffres)
PointAo = random.choice(ListeChiffres)
print("A(" + str(PointAa) + "," + str(PointAo) + ")")

while ReponseDemande == None:
    ReponseJoueur = input("Le point A est t'il sur la droite f(x),rep(y ou n): ")
    if ReponseJoueur == "y":
        ReponseDemande = 1
    elif ReponseJoueur == "n":
        ReponseDemande = 1
    else:
        continue

MembreDroite = ax * PointAa + b
if ReponseJoueur == "y" and PointAo == MembreDroite:
    print("JUSTE,Le point A est sur la droite f(x)")
elif ReponseJoueur == "y" and PointAo != MembreDroite:
    print("FAUX,Le point A n'est pas sur la droite f(x)")
elif ReponseJoueur == "n" and PointAo == MembreDroite:
    print("FAUX,La point A est sur la droite f(x)")
elif ReponseJoueur == "n" and PointAo != MembreDroite:
    print("JUSTE,Le point A n'est pas sur la droite f(x)")

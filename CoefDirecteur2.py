import random
listeNombres = list(range(-10 , 10+1))
listeNombres.remove(0)
suite = 0

xA = random.choice(listeNombres)
yA = random.choice(listeNombres)
print("A(" + str(xA) + "," + str(yA) + ")")

ax = random.choice(listeNombres)
b = random.choice(listeNombres)
print("y = " + str(ax) + "x + " + str(b))

while suite == 0:
    try:
        reponseJoueur = str(input("A appartient à la droite y (a ou ap) : "))
        if reponseJoueur == str(reponseJoueur):
            if str(reponseJoueur) == "a" or str(reponseJoueur) ==  "ap":
                suite = 1
    except SyntaxError:
        ...

# calculer yA

y = ax*xA + b

# Comparer les reponses

if y == b  and reponseJoueur == "a":
    print("Juste, Le point A appartient a la droite")
elif y == b and reponseJoueur == "ap":
    print("Faux,Le point A appartient a la droite")
elif y != b and reponseJoueur == "a":
    print("Faux, Le point A n'appartient pas a la droite")
elif y != b and reponseJoueur == "ap":
    print("Juste, Le point A n'appartient pas a la droite")
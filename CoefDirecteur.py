# Importation du module random qui servira plus tard
import random

# Variable qui seront utiliser plus tard
DeltaYPass = 0
DeltaXPass = 0

# Creation liste de nombres allant de -10 à 10
listeNombres = list(range(-10, 10 + 1)) 

# Retire le 0 pour empecher les division par 0
listeNombres.remove(0)

# choix du point xA, yA, xB, yB 
xA = random.choice(listeNombres)
yA = random.choice(listeNombres)
xB = random.choice(listeNombres)
yB = random.choice(listeNombres)

# Affiche les coordonné du point A et B
print("A("+str(xA)+","+str(yA)+")")
print("B("+str(xB)+","+str(yB)+")")

# L'ordinateur calcule delta Y et delta X
ordinateurDeltaY = yA - yB
ordinateurDeltaX = xA - xB

# Demande les reponses à l'utilisateur
while DeltaYPass == 0:    
    try:
        utilisateurDeltaY = int(input("Delta Y = "))
        if utilisateurDeltaY == int(utilisateurDeltaY):
            DeltaYPass = 1
    except ValueError:
        ...
print(str(utilisateurDeltaY) + "/?")

while DeltaXPass == 0 or utilisateurDeltaX == 0:
    try:
        utilisateurDeltaX = int(input("Delta X = "))
        if utilisateurDeltaX == int(utilisateurDeltaX):
            DeltaXPass = 1
    except ValueError:
        ...
print(str(utilisateurDeltaY)+"/"+str(utilisateurDeltaX))

# Comparer les reponses 
if ordinateurDeltaY == utilisateurDeltaY and ordinateurDeltaX == utilisateurDeltaX:
    print("")
    print("JUSTE")
else:
    print("")
    print("FAUX")
    print("La reponse est:")
    print(str(ordinateurDeltaY) + "/" + str(ordinateurDeltaX))

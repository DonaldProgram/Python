import random
afficheResultatN = 0
afficheResultatD = 0
afficheResultat = 0
reductionUser = []
reductionOrdinateur = []
userRepNumerateur2 = None
userRepDenominateur2 = None
listeChiffres = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("ax + b = cx + d")
print("x(a-c) = d - b")
print("x = (d-b) / (a-c)")
print('')
ax= random.choice(listeChiffres)
listeChiffres.remove(ax)
b = random.choice(listeChiffres)
listeChiffres.remove(b)
c = random.choice(listeChiffres)
listeChiffres.remove(c)
d = random.choice(listeChiffres)
listeChiffres.remove(d)

print("Resoudre :")
print(str(ax)+"x", '+('+str(b)+')','=', str(c)+"x",'+('+str(d)+')')
print("")

while afficheResultat == 0:
    try:
        userRepNumerateur = float(input("x = ?/ : "))
        if userRepNumerateur == float(userRepNumerateur):
            afficheResultatN = 1
    except ValueError:
        print("Ce n'est pas un nombre")
        continue

    while afficheResultat == 0: 
        if afficheResultatN == 1:
            try:
                userRepDenominateur = float(input("x = " + str(userRepNumerateur) + " /? : "))
                if userRepDenominateur == float(userRepDenominateur):
                    afficheResultat = 1
            except ValueError:
                print("Ce n'est pas un nombre")
print("Votre reponse : x = " + str(userRepNumerateur) + " / " + str(userRepDenominateur))

for a in listeChiffres:
    if (d-b) % a == 0 and (ax-c) % a == 0:
        reductionOrdinateur.append(a)
if len(reductionOrdinateur) > 0:
    repN = d-b
    repN /= max(reductionOrdinateur)
    repD = ax-c
    repD /= max(reductionOrdinateur)

print("")
print("Reponse :")
print(str(ax)+"x", '+('+str(b)+')','=', str(c)+"x",'+('+str(d)+')')
print(str(ax-c)+"x","=",str(d-b))
print("x =",str(repN)+"/"+str(repD))
print("")
print("Abscisse =",str(repN)+"/"+str(repD))
Ordonne = ax*(repN/repD)+b
print("Ordonne =" + str(Ordonne))


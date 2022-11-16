class Couleur:
    Bleu = '\033[94m' 
    Rouge = '\033[91m' 
    Normal = '\033[0m'
    Blanc = '\033[97m' 
    Noire = '\033[30m'
    Vert = '\033[32m'
    Orange = '\033[33m'
    Jaune = '\033[93m'
    Violet = '\033[95m'

# Coordonné point A( ; )
PasseOrdonneA = 0
while PasseOrdonneA == 0 :
    try:
        PointAa = float(input("A(?, ): ")) 
        if PointAa == float(PointAa):
            PasseOrdonneA = 1
    except ValueError:
        print(Couleur.Rouge + 'IL FAUT ENTRER UN NUMERO' + Couleur.Normal)

PasseAbscisseB = 0
while PasseAbscisseB == 0:
    try:
        PointAo = float(input('A(' + str(PointAa) +';?)'))
        if PointAo == float(PointAo):
            PasseAbscisseB = 1
    except ValueError:
        print(Couleur.Rouge + "IL FAUT UN NUMERO" + Couleur.Normal)

print('A(' + str(PointAa) + ';' + str(PointAo) + ')')

# Coordonné point B( ; )
PasseOrdonneB = 0
print('')
while PasseOrdonneB == 0:
    try:
        PointBa = float(input('B(?; )'))
        if PointBa == float(PointBa):
            PasseOrdonneB = 1
    except ValueError:
        print(Couleur.Rouge + 'IL FAUT UN NUMERO' + Couleur.Normal)

PasseAbscisseC = 0
while PasseAbscisseC == 0:
    try:
        PointBo = float(input('B(' + str(PointBa) +';?)'))
        if PointBo == float(PointBo):
            PasseAbscisseC = 1
    except ValueError:
        print(Couleur.Rouge + "IL FAUT UN NUMERO" + Couleur.Normal)

print('B(' + str(PointBa) + ';' + str(PointBo) + ')')

# Coordonne point C( ; )
PasseOrdonneC = 0
print('')
while PasseOrdonneC == 0:
    try:
        PointCa = float(input('C(?; )'))
        if PointCa == float(PointCa):
            PasseOrdonneC = 1
    except ValueError:
        print(Couleur.Rouge + 'IL FAUT UN NUMERO' + Couleur.Normal)

PasseFIN = 0
while PasseFIN == 0:
    try:
        PointCo = float(input('C(' + str(PointCa) +';?)'))
        if PointCo == float(PointCo):
            PasseFIN = 1
    except ValueError:
        print(Couleur.Rouge + "IL FAUT UN NUMERO" + Couleur.Normal)

print('C(' + str(PointCa) + ';' + str(PointCo) + ')')


# Calcule si les point sont alignés
try:
    Aab = (PointBo-PointAo)/(PointBa-PointAa)
    Aac = (PointCo-PointAo)/(PointCa-PointAa)
    print(Aab)
    print(Aac)
    if Aac == Aab:
        print("Les point sont alignés")
    else:
        print("Pas alignés")
except ZeroDivisionError:
    ...

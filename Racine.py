# Simp de racine

# Demande le chiffre de la racine et l'affiche
NombreRacine = int(input("Nombre a l'interieur de la racine : "))
print("racine de",NombreRacine)

# Decompose le nombre de la racine

listeReductions = []

for a in range(1, NombreRacine):
    if NombreRacine % a == 0:
        listeReductions.append(a)

print(listeReductions)

# le troisieme et l'avant dernier

nombreReductions1 = listeReductions[2]
nombreReductions2 = listeReductions[-2]

print(nombreReductions1)
print(nombreReductions2)


listeReductions1 = []
listeReductions2 = []

for a in range(1, nombreReductions1):
    if nombreReductions1 % a == 0:
        listeReductions1.append(a)

print(listeReductions1)

for a in range(1, nombreReductions2):
    if nombreReductions2 % a == 0:   
        listeReductions2.append(a)


print(listeReductions2)
if listeReductions1[-1] > nombreReductions2:
    print(nombreReductions2 ,'racine de', listeReductions1[1])
else:
    print(listeReductions1[1],'racine de', nombreReductions2)


    
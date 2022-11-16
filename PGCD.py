# Donner le PGCD de deux nombres

nb_1 = int(input(">> "))
nb_2 = int(input(">> "))

l1 = []
l2 = []

for i in range(1, nb_1):
    if nb_1 % i == 0:
        l1.append(i)

for a in range(1, nb_2):
    if nb_2 % a == 0:
        l2.append(a)

def listeCommun(l1, l2):
    l = []

    for i in l1:
        if i in l2:
            l.append(i)

    return l

if nb_1 != nb_2:
    print(max(listeCommun(l1, l2)))

elif nb_1 > nb_2:
    if nb_1 % nb_2 == 0:
        print(nb_2)

elif nb_1 < nb_2:
    if nb_2 % nb_1 == 0:
        print(nb_1)

elif nb_1 == nb_2:
    print(nb_1)            



# AdditionReductionDeFractions

n1 = int(input("Numerateur1 >> "))
d1 = int(input("Denominateur1 >> "))

n2 = int(input("Numerateur2 >> "))
d2 = int(input("Denominateur2 >> "))

n3 = n1 * d2 + n2 * d1
d3 = d1 * d2

print(" ")

listeReductions = []

for a in range(1, n3 + 1):
    if d3 % a == 0 and n3 % a == 0:
        listeReductions.append(a)

listeReductions = max(listeReductions)

nR = n3 / listeReductions
dR = d3 / listeReductions

print("Reponse N", nR)
print("Reponse D", dR)

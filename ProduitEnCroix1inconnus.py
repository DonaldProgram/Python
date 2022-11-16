# Effectuer un produit en croix avec une inconnus(x)
print("Pour mettre x taper 0")
Inconnus = 0

n1 = int(input("N1 >> "))
d1 = int(input("D1 >> "))

n2 = int(input("N2 >> "))
d2 = int(input("D2 >> "))

if n1 == 0:
    Nx = n1
    Inconnus += 1
if n2 == 0:
    Nx = n2
    Inconnus += 1
if d1 == 0:
    Nx = d1
    Inconnus += 1
if d2 == 0:
    Nx = d2
    Inconnus += 1

if Inconnus > 1:
    print("Il y a trop d'inconnus")

if Inconnus < 1:
    print("Il faut au moins une inconnus")

if Inconnus < 2 and Inconnus > 0:
    if Nx == n1:
        ProduitCR = (n2 * d1) / d2
        print(ProduitCR)

if Inconnus < 2 and Inconnus > 0:
    if Nx == n2:
        ProduitCR = (n1 * d2) / d1
        print(ProduitCR)

if Inconnus < 2 and Inconnus > 0:
    if Nx == d1:
        ProduitCR = (n1 * d2) / n2
        print(ProduitCR)

if Inconnus < 2 and Inconnus > 0:
    if Nx == d2:
        ProduitCR = (n2 * d1) / n1
        print(ProduitCR)
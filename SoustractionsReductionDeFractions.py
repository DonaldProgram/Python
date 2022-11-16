# Soustraire puis reduire deux fractions

# Recuperations des Fractions

n1 = int(input("Numerateur1>> "))
d1 = int(input("Denominateur1 >> "))

n2 = int(input("Numerateur2 >> "))
d2 = int(input("Denominateur2 >> "))

print(" ")

# Renomme les fractions (servira pour le calcul)

if n1 / d1 > n2 / d2:
    ng = n1 
    dg = d1
    np = n2 
    dp = d2
else:
    np = n1 
    dp = d1 
    ng = n2
    dg = d2

# Soustractions Fractions

n3 = ng * dp - np * dg
d3 = dg * dp 

# Reductions Fractions

Reductions = []

for a in range(1, n3 + 1):
    if n3 % a == 0 and d3 % a == 0:
        Reductions.append(a)


Reductions = max(Reductions)

n3 = n3 / Reductions
d3 = d3 / Reductions

if n2 == ng:
    print("-",n3)
    print(d3)
else:
    print(n3)
    print(d3)








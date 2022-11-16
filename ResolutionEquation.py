import random
Passe = None
Reduit = 0
liste = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reductions = []

ax = random.choice(liste)
b = random.choice(liste)

print("f(x) = 0")
print("ax + b = 0")

print(str(ax)+"x", "+("+ str(b) + ") = 0")
print(str(ax) + "x =", -b)

try:
    for a in liste:
        if b % a == 0 and ax % a == 0:
            reductions.append(a)
    b = b / max(reductions)
    ax = ax / max(reductions)
    print("x =", -b,"/",ax)
except ZeroDivisionError:
    print("x =",-b + "/",ax)
case1 = False
case2 = False
case3 = False
case4 = False
case5 = False
case6 = False

nombre1 = None
nombre2 = None
nombre3 = None
nombre4 = None
nombre5 = None
nombre6 = None

res1 = 1
res2 = 1
res3 = 1

reduction1_2 = []
reduction3_4 = []
reduction5_6 = []

def Tableau():
    print('|',nombre1,'| |',nombre3,'| |',nombre5,'|')
    print('|',nombre2,'| |',nombre4,'| |',nombre6,'|')
    print('|',res1,'| |',res2,'| |',res3,'|')

def calculer():  
    for a in range(1, nombre1 + 1):
        if nombre2 % a == 0 and nombre1 % a == 0:
            reduction1_2.append(a)

    res_01 = nombre1 / max(reduction1_2)
    res_02 = nombre2 / max(reduction1_2)
    res1 = res_01 / res_02
    
    for b in range(1, nombre3 + 1):
        if nombre4 % b == 0 and nombre3 % b == 0:
            reduction3_4.append(b)

    res_03 = nombre3 / max(reduction3_4)
    res_04 = nombre4 / max(reduction3_4)
    res2 = res_03 / res_04

    for c in range(1, nombre5 + 1):
        if nombre6 % c == 0 and nombre5 % c == 0:
            reduction5_6.append(c)

    res_05 = nombre5 / max(reduction5_6)
    res_06 = nombre6 / max(reduction5_6)
    res3 = res_05 / res_06
    Tableau()


while case1 != True:
    try:
        nombre1 = int(input("Case 1 -> "))
        case1 = True
        Tableau()
        print("")
    except ValueError:
        print("Ce n'est pas un nombre")

while case2 != True:
    try:
        nombre2 = int(input("Case 2 -> "))
        case2 = True
        Tableau()
        print("")
    except ValueError:
        print("Ce n'est pas un nombre")

while case3 != True:
    try:
        nombre3 = int(input("Case 3 -> "))
        case3 = True
        Tableau()
        print("")
    except ValueError:
        print("Ce n'est pas un nombre")

while case4 != True:
    try:
        nombre4 = int(input("Case 4 -> "))
        case4 = True
        Tableau()
        print("")
    except ValueError:
        print("Ce n'est pas un nombre")

while case5 != True:
    try:
        nombre5 = int(input("Case 5 -> "))
        case5 = True
        Tableau()
        print("")
    except ValueError:
        print("Ce n'est pas un nombre")

while case6 != True:
    try:
        nombre6 = int(input("Case 6 -> "))
        case6 = True
        Tableau()
        calculer()
        print("")
    except ValueError:
        print("Ce n'est pas un nombre")

# Theoreme de Thales

while True:
    l1 = int(input("Coté 1 petit >> "))
    l1c2 = int(input("Coté 1 grand >> "))
    
    l2 = int(input("Coté 2 petit >> "))
    l2c2 = int(input("Coté 2 grand >> "))
    
    l3 = int(input("Coté 3 petit >> "))
    l3c2 = int(input("Coté 3 grand >> "))

    if l1/l1c2 == l2/l2c2 == l3/l3c2:
        print("Votre triangle verifie le theoreme de Thales")
    else:
        print("Votre triangle ne verifie pas le theoreme de Thales")
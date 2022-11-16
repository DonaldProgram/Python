# Calculer la Vitesse

Choix = input("1, 2, 3 >> ")

if Choix == "1":
    # mètre par seconde
    Distance = float(input("Distance en mètre >> "))           
    Temps = float(input("Temps en seconde >> "))
    Reponse = Distance / Temps
    
    print(Reponse,"m/s")
    print(Reponse * 3.6,"Km/h")
# ok

elif Choix == "2":
    # Km par seconde
    Distance = float(input("Distance en Km >> "))
    Temps = float(input("Temps en seconde >> "))
    Reponse = Distance / Temps
    
    print(Reponse * 1000,"m/s")
    print(Reponse * 3600,"Km/h")
# ok

elif Choix == "3":
    # mètre par heure
    Distance = float(input("Distance en mètre >> "))
    Temps = float(input("Temps en heure >> "))
    Reponse = Distance / Temps

    print(Reponse / 3600,"m/s")
    print(Reponse / 1000,"Km/h")
# ok 

else:
    print("Mauvais chiffre")

    

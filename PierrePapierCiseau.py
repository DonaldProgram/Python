# jeu du pierre papier ciseau 
import random
Score = 0

while True:
    print("")
    Choix = str(input("pi, pa ou ci >> "))
    bot = random.choice(['Pierre', 'Papier', 'Ciseau'])

    if Choix == 'pi' and bot == 'Pierre':
        print("Egalité pas de point")
        print("Vôtre score est de", Score)

    elif Choix == 'pi' and bot == 'Papier':
        print("Perdu pas de point")
        print("Vôtre score est de", Score)

    elif Choix == 'pi' and bot == 'Ciseau':
        print("Gagné plus 1 point")
        Score += 1
        print("Vôtre score est de", Score)

    elif Choix == 'pa' and bot == 'Pierre':
        print("Gagné plus 1 point")
        Score += 1
        print("Vôtre score est de", Score)

    elif Choix == 'pa' and bot == 'Papier':
        print("Egalité pas de point")
        

    elif Choix == 'pa' and bot == 'Ciseau':
        print("Perdu pas de point")
        print("Vôtre score est de", Score)

    elif Choix == 'ci' and bot == 'Pierre':
        print("Perdu pas de point")
        print("Vôtre score est de", Score)

    elif Choix == 'ci' and bot == 'Papier':
        print("Gagné plus 1 point")
        Score += 1
        print("Vôtre score est de", Score)

    elif Choix == 'ci' and bot == 'Ciseau':
        print("Egalité pas de point")
        print("Vôtre score est de", Score)
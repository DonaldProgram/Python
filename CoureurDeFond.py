def distance(temps):
    if temps < 1:
        resultat = 15 * temps
    else:
        resultat = 12 * temps
    return resultat

print(distance(1.5))


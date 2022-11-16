def fonction1(a, b):
    global afficheMax

    liste = []
    e = b
    afficheMax = 0
    for i in range(1, a+1):
        if e * i > a:
            afficheMax = 1
        elif e*i <= a:
            b = e*i
            liste.append(b)        
    
    if afficheMax == 1:
        print(max(liste))

fonction1(40, 10)

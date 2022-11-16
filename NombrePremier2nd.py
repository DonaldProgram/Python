reponse = True
Nombre = 126552
for i in range(2, Nombre):
    if Nombre % i == 0:
        reponse = False

if reponse == False:
    print('Pas premier')
else:
    print("Premier")
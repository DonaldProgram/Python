# Devoir python seconde

A = 0
B = 1
C = 2
D = 3
E = 4
F = 5   
G = 6
H = 7
I = 8
J = 9
K = 10
L = 11
M = 12
N = 13
O = 14
P = 15
Q = 16
R = 17
S = 18
T = 19
U = 20
V = 21
W = 22
X = 23
Y = 24
Z = 25


def codage(x):
    resultat = 17 * x + 2 % 26
    if resultat > 25:
        while resultat > 25:
            resultat -= 26
    if resultat == 0:
        print('A')
    if resultat == 1:
        print('B')
    if resultat == 2:
        print('C')
    if resultat == 3:
        print('D')
    if resultat == 4:
        print('E')
    if resultat == 5:
        print('F')
    if resultat == 6:
        print('G')
    if resultat == 7:
        print('H')
    if resultat == 8:
        print('I')
    if resultat == 9:
        print('J')
    if resultat == 10:
        print('K')
    if resultat == 11:
        print('L')
    if resultat == 12:
        print('M')
    if resultat == 13:
        print('N')
    if resultat == 14:
        print('O')
    if resultat == 15:
        print('P')
    if resultat == 16:
        print('Q')
    if resultat == 17:
        print('R')
    if resultat == 18:
        print('S')
    if resultat == 19:
        print('T')
    if resultat == 20:
        print('U')
    if resultat == 21:
        print('V')
    if resultat == 22:
        print('W')
    if resultat == 23:
        print('X')
    if resultat == 24:
        print('Y')
    if resultat == 25:
        print('Z')

def decodage(x):
    decodage = 23 * x + 6 % 26
    if decodage > 25:
        while decodage > 25:
            decodage -= 26
    
    if decodage == 0:
        print('A')
    if decodage == 1:
        print('B')
    if decodage == 2:
        print('C')
    if decodage == 3:
        print('D')
    if decodage == 4:
        print('E')
    if decodage == 5:
        print('F')
    if decodage == 6:
        print('G')
    if decodage == 7:
        print('H')
    if decodage == 8:
        print('I')
    if decodage == 9:
        print('J')
    if decodage == 10:
        print('K')
    if decodage == 11:
        print('L')
    if decodage == 12:
        print('M')
    if decodage == 13:
        print('N')
    if decodage == 14:
        print('O')
    if decodage == 15:
        print('P')
    if decodage == 16:
        print('Q')
    if decodage == 17:
        print('R')
    if decodage == 18:
        print('S')
    if decodage == 19:
        print('T')
    if decodage == 20:
        print('U')
    if decodage == 21:
        print('V')
    if decodage == 22:
        print('W')
    if decodage == 23:
        print('X')
    if decodage == 24:
        print('Y')
    if decodage == 25:
        print('Z')
decodage(Y)
decodage(C)
decodage(N)
decodage(R)
decodage(S)
decodage(Y)
decodage(C)
decodage(N)
decodage(I)
decodage(O)
decodage(E)
decodage(S)
decodage(W)

# import des modules
import pygame
pygame.init()
#...

# creation de la fenetre
screen = pygame.display.set_mode((1920, 1080))
#...
# definir le nom du jeu
pygame.display.set_caption("JEUX")
#...





# import des images du jeu
arbre1 = pygame.image.load("sprite/arbre/1.png")
arbre2 = pygame.image.load("sprite/arbre/2.png")
arbre3 = pygame.image.load("sprite/arbre/3.png")
arbre4 = pygame.image.load("sprite/arbre/4.png")
arbre5 = pygame.image.load("sprite/arbre/5.png")
arbre6 = pygame.image.load("sprite/arbre/6.png")
arbre7 = pygame.image.load("sprite/arbre/7.png")

boutonSHOP = pygame.image.load("sprite/boutonSHOP.png")
MenuMagasin = pygame.image.load("sprite/Magasin.png")
#...

# definir les rectangles des differante image dont on a besoin
boutonSHOPrect = pygame.Rect(0, 0, 119, 51)
rectArbre1 = pygame.Rect(110, 475, 81, 132)
rectArbre2 = pygame.Rect(125, 358, 69, 114)
rectArbre3 = pygame.Rect(112, 260, 84, 96)
#...





# placer les differant objet
COOarbre1 = []
COOarbre2 = []
COOarbre3 = []
COOarbre4 = []
COOarbre5 = []
COOarbre6 = []
COOarbre7 = []
def MoveObjet():
    global COOarbre1, COOarbre2,COOarbre3, COOarbre4, COOarbre5, COOarbre6, COOarbre7, choixMagasin
    
    # recuperer la position de la souris
    position_mouse_x = pos[0] - 15
    position_mouse_y = pos[1] - 15
    #...
    # voir si le bouton gauche de la souris est pressé
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if choixMagasin == 'arbre1':
                COOarbre1.append((position_mouse_x, position_mouse_y))
            if choixMagasin == 'arbre2':
                COOarbre2.append((position_mouse_x, position_mouse_y))
            if choixMagasin == 'arbre3':
                COOarbre3.append((position_mouse_x, position_mouse_y))

    #...


    # si la longueur de la liste des coordonné est superieur a 0
    if len(COOarbre1) > 0:
        COOarbre1 = sorted(COOarbre1, key= lambda x: x[1])
        for positionArbre1 in COOarbre1:
            screen.blit(arbre1, positionArbre1)

    if len(COOarbre2) > 0:
        COOarbre2 = sorted(COOarbre2, key= lambda x: x[1])
        for positionArbre2 in COOarbre2:
            screen.blit(arbre2, positionArbre2)

    if len(COOarbre3) > 0:
        COOarbre3 = sorted(COOarbre3, key=lambda x: x[1])
        for positionArbre3 in COOarbre3:
            screen.blit(arbre3, positionArbre3)  
    #...

    
    # continuer d'afficher un autre objet au niveau de la souris
    if choixMagasin == 'arbre1':
        screen.blit(arbre1, (position_mouse_x, position_mouse_y))
    if choixMagasin == 'arbre2':
        screen.blit(arbre2, (position_mouse_x, position_mouse_y))
    if choixMagasin == 'arbre3':
        screen.blit(arbre3, (position_mouse_x, position_mouse_y))
    #...
#...





# definir la fonction pour pourvoir entrer dans le magasin
# variable qui sert a savoir si le bouton pour entrer dans le magasin
CliqueMagasin = False
choixMagasin = 'rien'
#...
def Magasin():
    global CliqueMagasin, choixMagasin
    # afficher le bouton pour entrer dans le shop
    if CliqueMagasin == False:
        screen.blit(boutonSHOP, (0, 0))
    #...

    # verifier si le bouton pour entrer dans le magasin est pressé
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1 and boutonSHOPrect.collidepoint(pos):
            CliqueMagasin = True
    #...

    # afficher le menu du magasin
    if CliqueMagasin == True:
        screen.blit(MenuMagasin, (0, 0))
    #...

    # voir si le joueur a cliquer sur un objet du magasin
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: 
            if rectArbre1.collidepoint(pos):
                choixMagasin = 'arbre1'
                CliqueMagasin = False
            if rectArbre2.collidepoint(pos):
                choixMagasin = 'arbre2'
                CliqueMagasin = False
            if rectArbre3.collidepoint(pos):
                choixMagasin = 'arbre3'
                CliqueMagasin = False
    #...
#...






# fonction gerant les fonction qui doivent etre appelé lors de la partie
def Game():
    # gerer les fonctions qui sont appelé lorsque l'on se trouve sur la carte
    # mettre la couleur d'arriere plan de la carte
    if CliqueMagasin == False:
        screen.fill((73, 255, 0))
    #...

        # appelé la fonction pour placé les arbres 3
        MoveObjet()
        #...
    #...

    # gerer ce qui se passe lorsque l'on se trouve dans le magasin
    # verifier que le bouton du magasin n'a pas été cliquer et si cliqué entrer dans magasin
    Magasin()
    #...
#...






# definir le nombre de fps du jeu
clock = pygame.time.Clock()
#...

# boucle du jeu
running = True
while running:
    # fermer la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #...

    # recuperer la position de la souris
    pos = pygame.mouse.get_pos()
    #...

    # appelé la fonction qui gere tous ce qui se passe dans le jeu
    Game()
    #...


    # mettre a jour l'ecran
    pygame.display.flip()
    #...
    # nombre de fps
    clock.tick(1000)
    #...


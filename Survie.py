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
arbreGROS = pygame.image.load("sprite/arbre/3.png")
boutonSHOP = pygame.image.load("sprite/boutonSHOP.png")
#...

# definir les rectangles des differante image dont on a besoin
boutonSHOPrect = pygame.Rect(0, 0, 119, 51)
#...





# placer les arbres 3
COOarbreGROS = []
def MoveArbre3():
    global COOarbreGROS
    
    # recuperer la position de la souris
    position_mouse_x = pos[0] - 15
    position_mouse_y = pos[1] - 15
    #...
    # voir si le bouton gauche de la souris est pressé
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            # ajouter la position de la souris a la liste des coordonné de l'arbre 3
            COOarbreGROS.append((position_mouse_x, position_mouse_y))
            #...
    #...


    # si la longueur de la liste des coordonné est superieur a 0
    if len(COOarbreGROS) > 0:
        # ranger dans l'ordre croissant des tuples en fonction du deuxieme element qui compose ces tuples
        COOarbreGROS = sorted(COOarbreGROS, key=lambda x: x[1])
        #...
        # afficher l'arbre gros au bonne coordonné
        for positionArbre3 in COOarbreGROS:
            screen.blit(arbreGROS, positionArbre3)  
        #...
    #...

    
    # continuer d'afficher un autre arbre 3 au niveau de la souris
    screen.blit(arbreGROS, (position_mouse_x, position_mouse_y))
    #...
#...





# definir la fonction pour pourvoir entrer dans le magasin
# variable qui sert a savoir si le bouton pour entrer dans le magasin
CliqueMagasin = False
#...
def Magasin():
    global CliqueMagasin
    # afficher le bouton pour entrer dans le shop
    if CliqueMagasin == False:
        screen.blit(boutonSHOP, (0, 0))
    #...

    # verifier si le bouton pour entrer dans le magasin est pressé
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1 and boutonSHOPrect.collidepoint(pos):
            CliqueMagasin = True
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
        MoveArbre3()
        #...
    #...

    # gerer ce qui se passe lorsque l'on se trouve dans le magasin
    # verifier que le bouton du magasin n'a pas été cliquer et si cliqué entrer dans magasin
    Magasin()
    #...
    # mettre la couleur d'arriere plan du magasin
    if CliqueMagasin == True:
        screen.fill((255, 255, 255))
    #...
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
    clock.tick(60)
    #...


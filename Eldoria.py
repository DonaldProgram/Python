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

    # mettre l'arriere plan en vert
    screen.fill((73, 255, 0))
    #...





    MoveArbre3()






    # mettre a jour l'ecran
    pygame.display.flip()
    #...
    # nombre de fps
    clock.tick(60)
    #...


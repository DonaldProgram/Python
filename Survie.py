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
# ok 

liste = []

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




    # test afficher l'arbreGROS
    posX = pos[0] - 15
    posY = pos[1] - 15
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            liste.append(posX)
            liste.append(posY)
    if len(liste) > 0:
        screen.blit(arbreGROS, (liste[0], liste[1]))  
    else:
        screen.blit(arbreGROS, (posX, posY))
    #...






    # mettre a jour l'ecran
    pygame.display.flip()
    #...


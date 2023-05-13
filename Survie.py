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
    x = pos[0] - 15
    y = pos[1] - 15
    screen.blit(arbreGROS, (x, y))
    #...





    # mettre a jour l'ecran
    pygame.display.flip()
    #...


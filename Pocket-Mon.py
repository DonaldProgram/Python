# creer un jeu du style pokemon
import pygame
pygame.init()

# creer la fenetre
screen = pygame.display.set_mode((1915, 1040))
pygame.display.set_caption("Pocket-Mon")
#...


# icon pokemon Menu txt 
MenuPokemonTxt = pygame.image.load("MenuPokemonTxt.png")
Motismadex = pygame.image.load("Motismadex.png")
#...


# boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # recuperer la position de la souris
    pos = pygame.mouse.get_pos()
    #...

    # recuperer les touches pressés
    pressed = pygame.key.get_pressed()
    #...

    # couleur de l'écran a blanc    
    screen.fill((255, 255, 255))
    #...
    
    screen.blit(MenuPokemonTxt, (300, 0))
    screen.blit(Motismadex, (20, 980))

    # mise a jour de l'ecran
    pygame.display.flip()
    #...
    

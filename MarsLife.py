import pygame
pygame.init()


# creer la fenetre
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("MarsLife")
#




# FONCTION DU MENU GO MARS


# creer le vaisseau qui permet de cliquer dans le menu
vaisseau = pygame.Rect(150, 150, 20, 15)
#...

# creer les textes a afficher sur le Menu
font = pygame.font.SysFont('monospace', 50)
Titre = font.render("MarsLife", 1, (255, 255, 255))
Help = font.render("Go to MARS", 1, (255, 255, 255))
#...

def GoMars():
    global Titre
    # gerer les touches presser
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP]:
        vaisseau.y -= 4
        vaisseau.width, vaisseau.height = 15, 20
    
    elif pressed[pygame.K_DOWN]:
        vaisseau.y += 4
        vaisseau.width, vaisseau.height = 15, 20
    
    elif pressed[pygame.K_LEFT]:
        vaisseau.x -= 4
        vaisseau.width, vaisseau.height = 20, 15
    
    elif pressed[pygame.K_RIGHT]:
        vaisseau.x += 4
        vaisseau.width, vaisseau.height = 20, 15
    #...
    
    
    # verifier si le vaisseau touche le texte du Menu "GO TO MARS"
    if vaisseau.x >= (1000-Help.get_width())/2-20 and vaisseau.x <= (1000-Help.get_width())/2-20 + Help.get_width() + 20:
        Titre = font.render("MarsLife2", 1, (255, 255, 255))
    else:
        Titre = font.render("MarsLife", 1, (255, 255, 255))
    #...
    
        
    # mettre l'ecran en noir
    screen.fill((0, 0, 0))        
    #...
    
    
    # afficher les textes sur le Menu
    screen.blit(Titre, ((1000-Titre.get_width())/2, (800-Titre.get_height())/2-300))
    screen.blit(Help, ((1000-Help.get_width())/2, (800-Help.get_height())/2-100))
    #...
    
    
    # afficher le joueur
    pygame.draw.rect(screen, (255, 255, 255), vaisseau)
    #...
#...






# gerer le nombre de fps
clock = pygame.time.Clock()
#...

# boucle du jeu
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    # afficher le menu GO TO MARS
    GoMars()
    #...
    
    
    
    
    # mettre a jour l'ecran
    pygame.display.flip()
    #...
    
    # gerer les fps
    clock.tick(60)
    #...
    
pygame.quit()
#...

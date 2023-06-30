import pygame
pygame.init()


# creer la fenetre
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("MarsLife")
#

# variable pour savoir quel menu doit etre afficher 
phase = 'MenuLancerJeu'

# FONCTION DU MENU GO MARS
# creer le vaisseau qui permet de cliquer dans le menu
vaisseau = pygame.Rect(150, 150, 20, 15)
#...

# creer les textes a afficher sur le Menu
font = pygame.font.SysFont('monospace', 50)

Titre = font.render("SYSTEME SOL-AIR", 1, (255, 255, 255))
LancerLeJeu = font.render("Explorer L'Infinie", 1, (255, 255, 255))
InfoJeu = font.render("Info", 1, (255, 255, 255))
#...

# creer les rects des textes du menu
rectGOTOMARS = LancerLeJeu.get_rect()
rectGOTOMARS.x = (1000-LancerLeJeu.get_width())/2
rectGOTOMARS.y = (800-LancerLeJeu.get_height())/2-50


rectINFO = InfoJeu.get_rect()
rectINFO.x = (1000-InfoJeu.get_width())/2
rectINFO.y = (800-InfoJeu.get_height())/2+25
#...

def MenuStartGame():
    global phase
    
    # verifier si le menu doit etre afficher
    if phase == 'MenuLancerJeu':
    #...
    
        # gerer les touches presser
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            vaisseau.y -= 5
            vaisseau.width, vaisseau.height = 15, 20
        
        elif pressed[pygame.K_DOWN]:
            vaisseau.y += 5
            vaisseau.width, vaisseau.height = 15, 20
        
        elif pressed[pygame.K_LEFT]:
            vaisseau.x -= 5
            vaisseau.width, vaisseau.height = 20, 15
        
        elif pressed[pygame.K_RIGHT]:
            vaisseau.x += 5
            vaisseau.width, vaisseau.height = 20, 15
        #...
        
        
        # verifier si le vaisseau touche des textes du menu
        # verifier si le vaisseau touche le texte du Menu "GO TO MARS"
        if rectGOTOMARS.colliderect(vaisseau):
            LancerLeJeu = font.render("-> EXPLORER L'INFINIE <-", 1, (255, 255, 255))
            if pressed[pygame.K_SPACE]:
                phase = 'explication'
        else:
            LancerLeJeu = font.render("Explorer L'Infinie", 1, (255, 255, 255))
        #...
        if rectINFO.colliderect(vaisseau):
            InfoJeu = font.render("-> INFO <-", 1, (255, 255, 255))            
        else:
            InfoJeu = font.render("Info", 1, (255, 255, 255))
        #...

        
        # afficher les textes sur le Menu
        screen.blit(Titre, ((1000-Titre.get_width())/2, (800-Titre.get_height())/2-300))
        screen.blit(LancerLeJeu, ((1000-LancerLeJeu.get_width())/2, (800-LancerLeJeu.get_height())/2-50))
        screen.blit(InfoJeu, ((1000-InfoJeu.get_width())/2, (800-InfoJeu.get_height())/2 + 25))    
        #...
        
        
        # afficher le vaisseau
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
            
    # mettre l'ecran en noir
    screen.fill((0, 0, 0))        
    #...
        
    
    
    
    # afficher le menu GO TO MARS
    MenuStartGame()
    #...
    
    
    
    
    # mettre a jour l'ecran
    pygame.display.flip()
    #...
    
    # gerer les fps
    clock.tick(60)
    #...
    
pygame.quit()
#...

import pygame
pygame.init()


# creer la fenetre
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("SOL-AIR")
#

# variable pour savoir quel menu doit etre afficher 
phase = 'MenuLancerJeu'
#...




# fonction pour gerer le vaisseau
# creer le vaisseau 
vaisseau = pygame.Rect(150, 150, 20, 15)
#...

#variable pour gerer la vitesse du vaisseau
vaisseau_speed = 5
#...

def move_vaisseau():
    # deplacer le vaisseau    
    if pressed[pygame.K_UP] and vaisseau.y >= vaisseau.height/2:
        vaisseau.y -= vaisseau_speed
        vaisseau.width, vaisseau.height = 15, 20
        
    elif pressed[pygame.K_DOWN] and vaisseau.y <= 800-vaisseau.height*1.5:
        vaisseau.y += vaisseau_speed
        vaisseau.width, vaisseau.height = 15, 20
        
    elif pressed[pygame.K_LEFT] and vaisseau.x >= vaisseau.width/2:
        vaisseau.x -= vaisseau_speed
        vaisseau.width, vaisseau.height = 20, 15
        
    elif pressed[pygame.K_RIGHT] and vaisseau.x <= 1000-vaisseau.width-10:
        vaisseau.x += vaisseau_speed
        vaisseau.width, vaisseau.height = 20, 15
    #...
    
    # afficher le vaisseau
    pygame.draw.rect(screen, (255, 255, 255), vaisseau)
    #...
#...





# FONCTION DU MENU START
# creer les textes a afficher sur le Menu
font = pygame.font.SysFont('monospace', 50)
font2 = pygame.font.SysFont('monospace', 20)

TexteTitreMenu = font.render("SYSTEME SOL-AIR", 1, (255, 255, 255))
texteLancerJeu = font.render("Explorer L'Infinie", 1, (255, 255, 255))
textInfoJeu = font.render("Info", 1, (255, 255, 255))

textFlecheHaut = font2.render("↑", 1, (255, 255, 255))
textFlecheBas = font2.render("↓", 1, (255, 255, 255))
textFlecheGauche = font2.render("←", 1, (255, 255, 255))
textFlecheDroite = font2.render("→", 1, (255, 255, 255))
textFlecheSpace = font2.render("Press Space", 1, (255, 255, 255))
#...

# creer les rects des textes du menu
RectLancerJeu = texteLancerJeu.get_rect()
RectLancerJeu.x = (1000-texteLancerJeu.get_width())/2
RectLancerJeu.y = (800-texteLancerJeu.get_height())/2-50


rectINFO = textInfoJeu.get_rect()
rectINFO.x = (1000-textInfoJeu.get_width())/2
rectINFO.y = (800-textInfoJeu.get_height())/2+25
#...

def MenuStartGame():
    global phase
    
    # verifier si le menu doit etre afficher
    if phase == 'MenuLancerJeu':
    #...
        
        # fonction gerer le vaisseau
        move_vaisseau()
        #...

        # verifier si le vaisseau touche des textes du menu
        # verifier si le vaisseau touche le texte du Menu "SYSTEME SOL-AIR"
        if RectLancerJeu.colliderect(vaisseau):
            screen.blit(textFlecheSpace, ((1000-textFlecheSpace.get_width())/2, 200))
            texteLancerJeu = font.render("-> EXPLORER L'INFINIE <-", 1, (255, 255, 255))
            if pressed[pygame.K_SPACE]:
                phase = 'EnvoieressourceTerreMars'
        else:
            texteLancerJeu = font.render("Explorer L'Infinie", 1, (255, 255, 255))
        #...
        
        if rectINFO.colliderect(vaisseau):
            screen.blit(textFlecheSpace, ((1000-textFlecheSpace.get_width())/2, 200))
            textInfoJeu = font.render("-> INFO <-", 1, (255, 255, 255))            
            if pressed[pygame.K_SPACE]:
                phase = 'info jeu'
        else:
            textInfoJeu = font.render("Info", 1, (255, 255, 255))
        #...

        
        # afficher les textes sur le Menu
        screen.blit(TexteTitreMenu, ((1000-TexteTitreMenu.get_width())/2, (800-TexteTitreMenu.get_height())/2-300))
        screen.blit(texteLancerJeu, ((1000-texteLancerJeu.get_width())/2, (800-texteLancerJeu.get_height())/2-50))
        screen.blit(textInfoJeu, ((1000-textInfoJeu.get_width())/2, (800-textInfoJeu.get_height())/2 + 25))    
        
        # afficher les touches a utiliser pour deplacer le vaisseau
        screen.blit(textFlecheHaut, (63, 730))
        screen.blit(textFlecheBas, (63, 760))
        screen.blit(textFlecheGauche, (40, 745))
        screen.blit(textFlecheDroite, (86, 745))
        #...
    #...
#...






# fonction du menu INFO
# definir les variables des textes a afficher sur le menu INFO
TitreInfo = font.render("INFO", 1, (255, 255, 255))
TexteQUITTERinfo = font.render("Quit", 1, (255, 255, 255))

TexteInfo1 = font2.render("Vous partez de la Terre en direction de Mars.", 1, (255, 255, 255))
TexteInfo2 = font2.render("Vous devez rendre Mars habitable et accueillir des Humains.", 1, (255, 255, 255))
TexteInfo3 = font2.render("- Vous pouvez vous aidez de la puissance du Soleil pour avoir de l'énergie.", 1, (255, 255, 255))
TexteInfo4 = font2.render("- Vous pouvez vous aidez de Jupiter pour avoir du gaz.", 1, (255, 255, 255))
TexteInfo5 = font2.render("- Vous pouvez vous aidez de Neptune pour avoir de l'eau.", 1, (255, 255, 255))
TexteInfo6_1 = font2.render("N'oubliez pas de bien choisir les choses que,", 1, (255, 255, 255))
TexteInfo6_2 = font2.render("vous souhaitez emportez dans la fusée qui vous emmènera sur Mars.", 1, (255, 255, 255))
TexteInfo7 = font2.render("Bonne chance !", 1, (255, 255, 255))
#...

# creer le rect du texte 'quit'
rectQUITinfo = TexteQUITTERinfo.get_rect()
#...


def InfoJeu():
    global phase
    
    # verifier si la fenetre de l'info du jeu doit etre afficher
    if phase == 'info jeu':
        # gerer le vaisseau
        move_vaisseau()
        #...
        
        # verifier si le vaisseau QUIT le menu info
        if rectQUITinfo.colliderect(vaisseau):
            screen.blit(textFlecheSpace, ((1000-textFlecheSpace.get_width())/2, 40))
            TexteQUITTERinfo = font.render("QUIT", 1, (255, 255, 255))
            if pressed[pygame.K_SPACE]:
                phase = 'MenuLancerJeu'
        else:
            TexteQUITTERinfo = font.render("Quit", 1, (255, 255, 255))
        #...


        # afficher les textes sur le menu info
        screen.blit(TitreInfo, ((1000-TitreInfo.get_width())/2, (800-TitreInfo.get_height())/2-300))
        
        screen.blit(TexteInfo1, ((1000-TexteInfo1.get_width())/2, (800-TexteInfo1.get_height())/2-200))
        screen.blit(TexteInfo2, ((1000-TexteInfo2.get_width())/2, (800-TexteInfo2.get_height())/2-150))
        screen.blit(TexteInfo3, ((1000-TexteInfo3.get_width())/2, (800-TexteInfo3.get_height())/2-100))
        screen.blit(TexteInfo4, ((1000-TexteInfo4.get_width())/2, (800-TexteInfo4.get_height())/2-50))
        screen.blit(TexteInfo5, ((1000-TexteInfo5.get_width())/2, (800-TexteInfo5.get_height())/2))
        screen.blit(TexteInfo6_1, ((1000-TexteInfo6_1.get_width())/2, (800-TexteInfo6_1.get_height())/2+50))
        screen.blit(TexteInfo6_2, ((1000-TexteInfo6_2.get_width())/2, (800-TexteInfo6_2.get_height())/2+75))
        screen.blit(TexteInfo7, ((1000-TexteInfo7.get_width())/2, (800-TexteInfo7.get_height())/2+125))
        
        
        screen.blit(TexteQUITTERinfo, (0, 0))
        #...
    #... 
#...





# definir la fonction pour gerer le decollage de la fusée vers Terre -> Mars
# variable servant a gerer l'espace restant dans la fusée
FuseeEnvoieTerreMars = 20
#...

# creer les rects de choix
rectChoixRessourceTerreMars = pygame.Rect(0, 0, 80, 80)
#...

def EnvoieRessourceTerreMars():
    if phase == 'EnvoieressourceTerreMars':
        pygame.draw.rect(screen, (255, 255, 255), rectChoixRessourceTerreMars)
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

    pressed = pygame.key.get_pressed()

    # mettre l'ecran en noir
    screen.fill((0, 0, 0))        
    #...
        
    
     
    
    # appeler toute les fonctions du jeu
    MenuStartGame()
    InfoJeu()
    EnvoieRessourceTerreMars()
    #...
    
    
    
    
    # mettre a jour l'ecran
    pygame.display.flip()
    #...
    
    # gerer les fps
    clock.tick(60)
    #...
    
pygame.quit()
#...

import pygame, random
pygame.init()


# creer la fenetre
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("SOL-AIR")
#

# changer l'icone de la fenetre
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
#...


# variable pour savoir quel menu doit etre afficher 
phase = 'MenuLancerJeu'
#...


# variables gerant les tailles de texte
font = pygame.font.SysFont('monospace', 50)
font2 = pygame.font.SysFont('monospace', 20)
font3 = pygame.font.SysFont('monospace', 40)
font4 = pygame.font.SysFont('monospace', 10)
font5 = pygame.font.SysFont('Monaco', 30)
#...







# fonction pour afficher le bouton de retour
# creer la fleche pour quitter
TexteQUITTER = font.render("←", 1, (255, 255, 255))
#...

# creer le rect du texte 'quit'
rectQUIT = TexteQUITTER.get_rect()
rectQUIT.x = 30
rectQUIT.y = 0
#...

def BoutonBack(phases):
    global phase, TexteQUITTER
    # verifier si le vaisseau QUIT le menu info
    if rectQUIT.colliderect(vaisseau):
        screen.blit(textFlecheSpace, ((1000-textFlecheSpace.get_width())/2, 40))
        TexteQUITTER = font.render("←", 1, (255, 255, 255))
        if pressed[pygame.K_SPACE]:
            phase = phases
        else:
            TexteQUITTER = font.render("←", 1, (255, 255, 255))
    #...
    
    # afficher la fleche
    screen.blit(TexteQUITTER, (30, 0))
    #...
#...






# fonction pour afficher le bouton lancer
# creer le texte du bouton lancer
TexteLancer = font5.render("Lancer", 1, (0, 0, 0))
#...

# creer le rect autour du bouton
rectLancer = pygame.Rect(930, 780, 70, 20)
#...

textFlecheSpace = font2.render("Press Space", 1, (255, 255, 255))

def BoutonLancerPhase(phases):
    global textFlecheSpace, TexteLancer, phase
    
    # afficher le rect autour du texte
    pygame.draw.rect(screen, (255, 255, 255), rectLancer)
    #...
    
    # afficher le texte sur le rect
    screen.blit(TexteLancer, (930, 780))
    #...
    
    if rectLancer.colliderect(vaisseau):
        screen.blit(textFlecheSpace, ((850, 700)))
        if pressed[pygame.K_SPACE]:
            phase = phases
#...








# fonction pour afficher des etoile a l'ecran
# liste pour gerer les coordonnée des etoile a afficher
liste_etoile = []
#...


# boucle pour ajouter toute les etoile a la liste
for a in range(0, 500):
    if random.randint(0, 2) == 0:
        etoile_x = random.randint(0, 1000)
        etoile_y = random.randint(0, 1000)
        liste_etoile.append((etoile_x, etoile_y))
#...

# creer le point representant l'etoile
Etoile = font4.render('.', 1, (255, 255, 255))
#...

def afficher_etoile():
    for a in range(len(liste_etoile)):
        screen.blit(Etoile, liste_etoile[a])   
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








# fonction pour afficher le tuto pour deplacer le vaisseau
textFlecheHaut = font3.render("↑", 1, (255, 255, 255))
textFlecheBas = font3.render("↓", 1, (255, 255, 255))
textFlecheGauche = font3.render("←", 1, (255, 255, 255))
textFlecheDroite = font3.render("→", 1, (255, 255, 255))

def afficher_fleche_tuto_vaisseau():
    # afficher les touches a utiliser pour deplacer le vaisseau
    screen.blit(textFlecheHaut, (40, 730))
    screen.blit(textFlecheBas, (40, 760))
    screen.blit(textFlecheGauche, (23, 745))
    screen.blit(textFlecheDroite, (57, 745))
    #...
#...







# FONCTION DU MENU START
# creer les textes a afficher sur le Menu
TexteTitreMenu = font.render("SYSTEME SOL-AIR", 1, (255, 255, 255))
texteLancerJeu = font.render("Explorer L'Infinie", 1, (255, 255, 255))
textInfoJeu = font.render("Info", 1, (255, 255, 255))
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

        # afficher le tuto pour deplacer le vaisseau
        afficher_fleche_tuto_vaisseau()
        #...
        
        # verifier si le vaisseau touche des textes du menu
        # verifier si le vaisseau touche le texte du Menu "SYSTEME SOL-AIR"
        if RectLancerJeu.colliderect(vaisseau):
            screen.blit(textFlecheSpace, ((1000-textFlecheSpace.get_width())/2, 200))
            texteLancerJeu = font.render("-> EXPLORER L'INFINIE <-", 1, (255, 255, 255))
            if pressed[pygame.K_SPACE]:
                phase = 'ChoixDifficulté'
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
    #...
#...








# fonction du menu INFO
# definir les variables des textes a afficher sur le menu INFO
TitreInfo = font.render("INFO", 1, (255, 255, 255))

TexteInfo1 = font2.render("Vous partez de la Terre en direction de Mars.", 1, (255, 255, 255))
TexteInfo2 = font2.render("Vous devez rendre Mars habitable et accueillir des Humains.", 1, (255, 255, 255))
TexteInfo3 = font2.render("- Vous pouvez vous aidez de la puissance du Soleil pour avoir de l'énergie.", 1, (255, 255, 255))
TexteInfo4 = font2.render("- Vous pouvez vous aidez de Jupiter pour avoir du gaz.", 1, (255, 255, 255))
TexteInfo5 = font2.render("- Vous pouvez vous aidez de Neptune pour avoir de l'eau.", 1, (255, 255, 255))
TexteInfo6_1 = font2.render("N'oubliez pas de bien choisir le mode que", 1, (255, 255, 255))
TexteInfo6_2 = font2.render("vous voulez (changement de difficulté.)", 1, (255, 255, 255))
TexteInfo7 = font2.render("La monnaie des étoiles et le AC ou AstroCredit.", 1, (255, 255, 255))
TexteInfo8 = font2.render("Bonne chance !", 1, (255, 255, 255))
#...


def InfoJeu():
    global phase
    # verifier si la fenetre de l'info du jeu doit etre afficher
    if phase == 'info jeu':
        # gerer le vaisseau
        move_vaisseau()
        #...
        
        # afficher le tuto pour deplacer le vaisseau
        afficher_fleche_tuto_vaisseau()
        #...
        
        # afficher le bouton de retour
        BoutonBack('MenuLancerJeu')
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
        screen.blit(TexteInfo8, ((1000-TexteInfo8.get_width())/2, (800-TexteInfo8.get_height())/2+200))
        #...
    #... 
#...








# definir la fonction pour gerer le decollage de la fusée vers Terre -> Mars
# variable servant a gerer les texte des modes de jeu
TexteModeFacile = font3.render("Easy", 1, (255, 255, 255))
InfoModeFacile1 = font2.render("+ 5 000 000 AC", 1, (255, 255, 255))
InfoModeFacile2 = font2.render("+ 10 000 AC toutes les secondes", 1, (255, 255, 255))
InfoModeFacile3 = font2.render("+ Objets déjà construit sur Mars", 1, (255, 255, 255))
InfoModeFacile4 = font2.render("+ Energie illimité", 1, (255, 255, 255))
InfoModeFacile5 = font2.render("+ Aucun impact de météorite", 1, (255, 255, 255))
InfoModeFacile6 = font2.render("+ Aucun impact d'astéorïde", 1, (255, 255, 255))
InfoModeFacile7 = font2.render("+ Aucune maladie", 1, (255, 255, 255))

TexteModeNormal = font3.render("Normal", 1, (255, 255, 255))
InfoModeNormal1 = font2.render("+ 3 000 000 AC", 1, (255, 255, 255))
InfoModeNormal2 = font2.render("+ 6 000 AC toutes les secondes", 1, (255, 255, 255))
InfoModeNormal3 = font2.render("+ Aucun impact d'astéroïde", 1, (255, 255, 255))

TexteModeHard = font3.render("Hard", 1, (255, 255, 255))
InfoModeHard1 = font2.render("+ 1 000 000 AC", 1, (255, 255, 255))
InfoModeHard2 = font2.render("+ 2 000 AC toutes les secondes", 1, (255, 255, 255))
InfoModeHard3 = font2.render("+ Maladie en plus", 1, (255, 255, 255))

TexteModeCreatif = font3.render("Creatif", 1, (255, 255, 255))
InfoModeCreatif1 = font2.render("+ ∞ AC", 1, (255, 255, 255)) 
#...

# rects des textes de difficulté
rectTexteFacile = TexteModeFacile.get_rect()
rectTexteFacile.x = 80
rectTexteFacile.y = 50

rectTexteNormal = TexteModeNormal.get_rect()
rectTexteNormal.x = 550
rectTexteNormal.y = 50

rectTexteHard = TexteModeHard.get_rect()
rectTexteHard.x = 80
rectTexteHard.y = 400

rectTexteCreatif = TexteModeCreatif.get_rect()
rectTexteCreatif.x = 550
rectTexteCreatif.y = 400
#...

# variable pour connaitre le mode choisi
ChoixMode = None
#...

def ChoixDifficulté():
    global phase, ChoixMode, TexteModeFacile,  TexteModeNormal, TexteModeHard, TexteModeCreatif
    if phase == 'ChoixDifficulté':
        
        # afficher le bouton pour lancer
        BoutonLancerPhase('MenuLancerJeu')
        #...
        
        # fonction pour gerer le vaisseau
        move_vaisseau()
        #...
            
        # afficher la fleche pour quitter le menu
        BoutonBack("MenuLancerJeu")
        #...
        
        # afficher les textes a l'ecran
        # mode easy
        screen.blit(TexteModeFacile, (80, 50))
        screen.blit(InfoModeFacile1, (60, 100))
        screen.blit(InfoModeFacile2, (60, 130))
        screen.blit(InfoModeFacile3, (60, 160))
        screen.blit(InfoModeFacile4, (60, 190))
        screen.blit(InfoModeFacile5, (60, 220))
        screen.blit(InfoModeFacile6, (60, 250))
        screen.blit(InfoModeFacile7, (60, 280))
        #...
        
        # mode normal
        screen.blit(TexteModeNormal, (550, 50))
        screen.blit(InfoModeNormal1, (530, 100))
        screen.blit(InfoModeNormal2, (530, 130))
        screen.blit(InfoModeNormal3, (530, 160))
        #...
        
        # mode hard
        screen.blit(TexteModeHard, (80, 400))
        screen.blit(InfoModeHard1, (60, 450))
        screen.blit(InfoModeHard2, (60, 480))
        screen.blit(InfoModeHard3, (60, 510))
        #...
        
        # mode creatif
        screen.blit(TexteModeCreatif, (550, 400))
        screen.blit(InfoModeCreatif1, (530, 450))
        #...
        
       # si le vaisseau choisi le texte easy
        if rectTexteFacile.colliderect(vaisseau):     
            if pressed[pygame.K_SPACE]:
                ChoixMode = "Facile"
                TexteModeFacile = font3.render("→ EASY ←", 1, (255, 255, 255))
        #... 
        
        # si le vaisseau choisi le texte easy
        if rectTexteNormal.colliderect(vaisseau):             
            if pressed[pygame.K_SPACE]:
                ChoixMode = "Normal"
                TexteModeNormal = font3.render("→ NORMAL ←", 1, (255, 255, 255))
        #... 
        
        # si le vaisseau choisi le texte hard
        if rectTexteHard.colliderect(vaisseau):             
            if pressed[pygame.K_SPACE]:
                ChoixMode = "Hard"
                TexteModeHard = font3.render("→ HARD ←", 1, (255, 255, 255))
        #... 
        
        # si le vaisseau choisi le texte creatif
        if rectTexteCreatif.colliderect(vaisseau):             
            if pressed[pygame.K_SPACE]:
                ChoixMode = "Creatif"
                TexteModeCreatif = font3.render("→ Creatif ←", 1, (255, 255, 255))
        #... 
        
        # remettre les texte par defaut si il ne sont pas selectionné
        if ChoixMode == "Facile":
                TexteModeNormal = font3.render("Normal", 1, (255, 255, 255))  
                TexteModeHard = font3.render("Hard", 1, (255, 255, 255))
                TexteModeCreatif = font3.render("Creatif", 1, (255, 255, 255))
                       
        if ChoixMode == "Normal":
                TexteModeFacile = font3.render("Easy", 1, (255, 255, 255))   
                TexteModeHard = font3.render("Hard", 1, (255, 255, 255))    
                TexteModeCreatif = font3.render("Creatif", 1, (255, 255, 255))
                
        if ChoixMode == "Hard": 
            TexteModeFacile = font3.render("Easy", 1, (255, 255, 255))   
            TexteModeNormal = font3.render("Normal", 1, (255, 255, 255))  
            TexteModeCreatif = font3.render("Creatif", 1, (255, 255, 255))
        
        if ChoixMode == "Creatif":
            TexteModeFacile = font3.render("Easy", 1, (255, 255, 255))   
            TexteModeNormal = font3.render("Normal", 1, (255, 255, 255))
            TexteModeHard = font3.render("Hard", 1, (255, 255, 255))    
        #...
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

    pressed = pygame.key.get_pressed()

    # mettre l'ecran en noir
    screen.fill((0, 0, 0))        
    #...
        
    
     
    
    # appeler toute les fonctions du jeu
    MenuStartGame()
    InfoJeu()
    ChoixDifficulté()
    #...
    
    # afficher les etoiles a l'ecran
    afficher_etoile()
    #...
    

    
    # mettre a jour l'ecran
    pygame.display.flip()
    #...
    
    # gerer les fps
    clock.tick(60)
    #...
    
pygame.quit()
#...

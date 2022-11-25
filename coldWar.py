# jeu cold war
import pygame, time
pygame.init()

# fenetre
screen = pygame.display.set_mode((1915, 1080))
pygame.display.set_caption("COLD-WAR")

# image
triangleMENU = pygame.image.load("triangleMENU.png")

# rectangles du menu
police = pygame.font.SysFont("Monospace", 80)
Mots_Menu = police.render("MENU", 1, (255, 0, 0))
Mots_start = police.render("Start", 1, (255, 0, 0))
Mots_Parametre = police.render("Parametres", 1, (255, 0, 0))


# rectangle des joueurs
rectJoueur1 = pygame.Rect(15, 480, 25, 108)
rectJoueur2 = pygame.Rect(1875, 480, 25, 108)

balleRouge = pygame.image.load("balleRouge.png")

jeu = False
# fait la musique de fond
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

clic = pygame.mixer.Sound("clic.mp3")
clic.set_volume(0.2)

# variable running qui fait tourner la boucle du jeu
running = True
parametre = 0
# Fonction du menu
menu = True
triangleMENUhei = 1
def Menu():
    global menu, jeu, parametre
    if menu == True:
        global triangleMENUhei
        # affiche le menu
        pressed = pygame.key.get_pressed()
        
        screen.fill((0, 0, 0))
        
        if triangleMENUhei == 1:
            screen.blit(triangleMENU, (740, 405))
            if pressed[pygame.K_RETURN]:
                clic.play()
                jeu = True
                menu = False
        if triangleMENUhei == 0:
            screen.blit(triangleMENU, (650, 505))
            if pressed[pygame.K_RETURN]:
                clic.play()
                parametre = True
                menu = False


        if pressed[pygame.K_UP]:
            triangleMENUhei = 1

        if pressed[pygame.K_DOWN]:
            triangleMENUhei = 0


        screen.blit(Mots_Menu, (835, 0))
        screen.blit(Mots_start, (800, 400))
        screen.blit(Mots_Parametre, (720, 500))
        pygame.display.flip()


def Parametre():
    global parametre, menu
    if parametre == 1:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            clic.play()
            menu = True
            parametre = 0
        police = pygame.font.SysFont("Monospace", 50)
        Mots_Parametre = police.render("Parametres", 1, (255, 0, 0))

        police = pygame.font.SysFont("Monospace", 25)
        Mots_Echap = police.render("Echap pour aller au menu", 1, (255, 0, 0))

        police = pygame.font.SysFont("Monospace", 50)

        TexteJoueur1_1 = police.render("JOUEUR 1", 1, (255, 0, 0))
        police = pygame.font.SysFont("Monospace", 30)

        TexteJoueur1_2 = police.render("Deplacement :", 1, (255, 0, 0))
        TexteJoueur1_3 = police.render("HAUT : z", 1, (255, 0, 0))
        TexteJoueur1_4 = police.render("BAS : s", 1, (255, 0, 0))
        TexteJoueur1_5 = police.render("TIRER : espace", 1, (255, 0, 0))
        
        police = pygame.font.SysFont("Monospace", 50)
        TexteJoueur2_1 = police.render("JOUEUR 2", 1, (0, 0, 255))

        police = pygame.font.SysFont("Monospace", 30)
        TexteJoueur2_2 = police.render("Deplacement :", 1, (0, 0, 255))
        TexteJoueur2_3 = police.render("HAUT : fleche haut", 1, (0, 0, 255))
        TexteJoueur2_4 = police.render("BAS : fleche bas", 1, (0, 0, 255))
        TexteJoueur2_5 = police.render("TIRER : entré", 1, (0, 0, 255))

        
        screen.fill((0, 0, 0))

        screen.blit(Mots_Parametre, (800, 0))
        screen.blit(Mots_Echap, (0, 0))
        
        # joueur 1
        screen.blit(TexteJoueur1_1, (150, 250))
        screen.blit(TexteJoueur1_2, (0, 320))
        screen.blit(TexteJoueur1_3, (50, 370))
        screen.blit(TexteJoueur1_4, (50, 405))
        screen.blit(TexteJoueur1_5, (50, 440))

        # joueur 2
        screen.blit(TexteJoueur2_1, (1375, 250))
        screen.blit(TexteJoueur2_2, (1525, 320))
        screen.blit(TexteJoueur2_3, (1575, 370))
        screen.blit(TexteJoueur2_4, (1575, 405))
        screen.blit(TexteJoueur2_5, (1575, 440))


        pygame.display.flip()

# compte a rebours du debut
rebours = 3
tir = 0
a = 0
positionJoueurRougey = 0


def Jeu():
    global rebours, tir, a, positionJoueurRougey

        
    
    global jeu, menu
    if jeu == True:
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 0, 0), rectJoueur1)
        pygame.draw.rect(screen, (0, 0, 255), rectJoueur2)
        
        pressed = pygame.key.get_pressed()
        # deplacement joueur 1
        if rectJoueur1.y > 0: # gere les collisions du joueur rouge en haut
            if pressed[pygame.K_z]:
                rectJoueur1.y -= 13
        if rectJoueur1.y < 902: # gere les collision du joueur rouge en bas
            if pressed[pygame.K_s]:
                rectJoueur1.y += 13

        if rectJoueur2.y > 0: # gere les collisions du joueur bleu en haut
            if pressed[pygame.K_UP]:
                rectJoueur2.y -= 13
        if rectJoueur2.y < 902: # gere les collision du joueur bleu en bas
            if pressed[pygame.K_DOWN]:
                rectJoueur2.y += 13

        pointBallx = rectJoueur1.x + 70
        pointBally = rectJoueur1.y + 54

        if tir == 0:
            if pressed[pygame.K_SPACE]:
                tir = 1
                a = 0
                positionJoueurRougey = rectJoueur1.y + 54
                pointBallx = rectJoueur1.x + 20
        
        a += 25
        if tir >= 1:
            pointBallx += a
            screen.blit(balleRouge, (pointBallx, positionJoueurRougey))
        if pointBallx > 2000:
            tir = 0
            a = 0

        pygame.display.flip()
    
    if rebours != -1:
        police = pygame.font.SysFont("Monospace", 150)
        CompteRebours = police.render(str(rebours), 1, (255, 255, 255))
        clic.play()
        screen.blit(CompteRebours, (880, 300))
        pygame.display.flip()
        time.sleep(1)
        rebours -= 1
        


# boucle du jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0)) 

    if menu == True:
        Menu()
    if parametre == True:
        Parametre()
    if jeu == True:
        Jeu()    


    pygame.display.flip()


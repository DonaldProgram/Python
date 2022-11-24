# jeu cold war
import pygame
pygame.init()

# fenetre
screen = pygame.display.set_mode((1915, 1080))

# image
triangleMENU = pygame.image.load("triangleMENU.png")

# rectangles du menu
police = pygame.font.SysFont("Monospace", 80)
Mots_Menu = police.render("MENU", 1, (255, 0, 0))
Mots_start = police.render("Start", 1, (255, 0, 0))
Mots_Parametre = police.render("Parametre", 1, (255, 0, 0))


# rectangle des joueurs
rectJoueur1 = pygame.Rect(15, 480, 25, 108)


# fait la musique de fond
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.15)

clic = pygame.mixer.Sound("clic.mp3")
clic.set_volume(0.2)

# variable running qui fait tourner la boucle du jeu
running = True
parametre = 0
# Fonction du menu
menu = True
triangleMENUhei = 1
def Menu():
    global triangleMENUhei
    # affiche le menu
    pressed = pygame.key.get_pressed()
    
    screen.fill((0, 0, 0))
    
    if triangleMENUhei == 1:
        screen.blit(triangleMENU, (740, 405))
        if pressed[pygame.K_RETURN]:
            clic.play()
            # lance le jeu
    if triangleMENUhei == 0:
        screen.blit(triangleMENU, (650, 505))
        if pressed[pygame.K_RETURN]:
            clic.play()
            parametre = 1
    
    if pressed[pygame.K_UP]:
        triangleMENUhei = 1

    if pressed[pygame.K_DOWN]:
        triangleMENUhei = 0


    screen.blit(Mots_Menu, (835, 0))
    screen.blit(Mots_start, (800, 400))
    screen.blit(Mots_Parametre, (720, 500))
    pygame.display.flip()



# boucle du jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0)) 

    if menu == True:
        Menu()
    else:
        screen.fill((0, 255, 255))
    pygame.display.flip()


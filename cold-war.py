import pygame
pygame.init()

# création de la fenêtre
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('COLD-WAR')
# ...


# définir les différents textes à afficher
font = pygame.font.SysFont('Courier New', 90)
texte_titre = font.render('COLD-WAR', True, (255, 0, 0))

font = pygame.font.SysFont('Courier New', 70)
texte_jouer = font.render('JOUER', True, (255, 0, 0))
texte_miroir = font.render('MIROIR', True, (255, 0, 0))
texte_parametre = font.render('PARAMETRE', True, (255, 0, 0))
fleche_choix = font.render('->', True, (255, 0, 0))
# ...


# variable choix permettant de sélectionner les différents textes
choix = 1
# ...

# definir une variable delay pour patientez un peu
delay = 200
#...

# fonction pour gérer le menu
def Menu(pressed):
    global texte_jouer, texte_miroir, texte_parametre, choix, last_change

    # afficher la flèche du choix
    if choix == 1:
        screen.blit(fleche_choix, (750, 350))
    if choix == 2:
        screen.blit(fleche_choix, (725, 435))
    if choix == 3:
        screen.blit(fleche_choix, (670, 520))
    # ...

    # afficher les textes sur le menu
    screen.blit(texte_titre, ((1920 - texte_titre.get_width()) / 2, 50))
    screen.blit(texte_jouer, ((1920 - texte_jouer.get_width()) / 2, 350))
    screen.blit(texte_miroir, ((1920 - texte_miroir.get_width()) / 2, 435))
    screen.blit(texte_parametre, ((1920 - texte_parametre.get_width()) / 2, 520))
    # ...

    # déplacer la flèche de choix si des touches sont pressées
    if pressed[pygame.K_DOWN] and pygame.time.get_ticks()-last_change >= delay:
        if choix != 3:
            choix += 1
            last_change = pygame.time.get_ticks()
    if pressed[pygame.K_UP] and pygame.time.get_ticks()-last_change >= delay:
        if choix != 1:
            choix -= 1
            last_change = pygame.time.get_ticks()

    # ...
# ...




# variable last_change qui sert a savoir le temps ecoulé depuis un certain moment
last_change = pygame.time.get_ticks()
#...

# boucle du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # récupérer les touches pressées
    pressed = pygame.key.get_pressed()
    #...

    # arriere plan en noir
    screen.fill((0, 0, 0))
    #...




    # appeler la fonction du menu
    Menu(pressed)
    # ...




    # mettre à jour l'écran
    pygame.display.flip()
    #...
# ...

pygame.quit()

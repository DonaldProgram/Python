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




# variable choixMenu permettant de sélectionner les différents textes
choixMenu = 1
# ...

# definir une variable delay pour patientez un peu
delay = 200
#...

# fonction pour gérer le menu
choixOnglet = 'MenuMenu'
def Menu(pressed):
    global texte_jouer, texte_miroir, texte_parametre, choixMenu, last_change, choixOnglet

    # afficher la flèche du choixMenu
    if choixMenu == 1:
        screen.blit(fleche_choix, (750, 350))
    if choixMenu == 2:
        screen.blit(fleche_choix, (725, 435))
    if choixMenu == 3:
        screen.blit(fleche_choix, (670, 520))
    # ...

    # afficher les textes sur le menu
    screen.blit(texte_titre, ((1920 - texte_titre.get_width()) / 2, 50))
    screen.blit(texte_jouer, ((1920 - texte_jouer.get_width()) / 2, 350))
    screen.blit(texte_miroir, ((1920 - texte_miroir.get_width()) / 2, 435))
    screen.blit(texte_parametre, ((1920 - texte_parametre.get_width()) / 2, 520))
    # ...

    # déplacer la flèche de choixMenu si des touches sont pressées
    if pressed[pygame.K_DOWN] and pygame.time.get_ticks()-last_change >= delay:
        if choixMenu != 3:
            choixMenu += 1
            last_change = pygame.time.get_ticks()
    if pressed[pygame.K_UP] and pygame.time.get_ticks()-last_change >= delay:
        if choixMenu != 1:
            choixMenu -= 1
            last_change = pygame.time.get_ticks()

    # verifier si la touche entré est pressé
    if pressed[pygame.K_RETURN] and choixMenu == 1:
        choixOnglet = 'MenuJouer'
    # ...
    #...
# ...






# fonction qui gere le choixMenu entre 1c1 ou 1cBOT
choixPartie = 1
font2 = pygame.font.SysFont('Courier New', 107)
texte_jouer2 = font2.render('JOUER', True, (255, 0, 0))
texte_1c1 = font2.render('1v1', True, (255, 0, 0))
texte_1cBOT = font2.render('1vBOT', True, (255, 0, 0))
font2 = pygame.font.SysFont("Courier New", 100)
fleche_choix2 = font2.render('->', True, (255, 0, 0))

choix_modes = 0

def ChoixPartie():    
    global choixPartie, texte_1c1, texte_jouer, last_change
    # afficher les boutons du choixMenu entré 1c1 ou 1cBOT
    screen.blit(texte_jouer2, ((1920 - texte_jouer2.get_width()) / 2, 15))
    screen.blit(texte_1c1, ((1920 - texte_1c1.get_width()) / 2, 350))
    screen.blit(texte_1cBOT, ((1920 - texte_1cBOT.get_width()) / 2, 450))

    #...

    # gerer la fleche en fonction des touches pressé
    if pressed[pygame.K_DOWN] and pygame.time.get_ticks()-last_change >= delay:
        if choixPartie != 2:
            choixPartie += 1
            last_change = pygame.time.get_ticks()
    if pressed[pygame.K_UP] and pygame.time.get_ticks()-last_change >= delay:
        if choixPartie != 1:
            choixPartie -= 1
            last_change = pygame.time.get_ticks()
    
    if choixPartie == 1:
        screen.blit(fleche_choix2, (720, 350))
    if choixPartie == 2:
        screen.blit(fleche_choix2, (670, 450))
    #...

    # verifier si la touche entré est pressé
    if pressed[pygame.K_RETURN] and choix == 1:
        choixOnglet = 'MenuChoixPartie'
    # ...

#...



# fonction gerant le 1c1
joueur = pygame.Surface((22, 130))
joueur.fill((255, 255, 255))

y1 = 540-joueur.get_height()
y2 = 540-joueur.get_height()

def v1():
    # afficher les deux joueur
    screen.blit(joueur, (15, y1))
    screen.blit(joueur, (1882, y2))
    #... 
#...




# fonction gerant les differante fonctions a appelé lors du 
def Game():
    
    # appeler la fonction menu au debut de la partie
    if choixOnglet == 'MenuMenu':
        Menu(pressed)
    #...

    # appeler la fonction du choixMenu de la partie
    elif choixOnglet == 'MenuJouer':
        ChoixPartie()
    #...

    elif choixOnglet == 'MenuChoixPartie':
        v1()
#...






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




    # appeler la fonction Game
    Game()
    # ...
        



    # mettre à jour l'écran
    pygame.display.flip()
    #...
# ...

pygame.quit()

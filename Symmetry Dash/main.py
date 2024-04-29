import pygame
pygame.init()

# créer la fenetre
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Symmetry Dash')


# variable servant a savoir la phase de jeu en cours
phase = 'Menu Principal'

# créer toutes les polices
font_arial_black_15 = pygame.font.SysFont('Arial Black', 15)
font_arial_black_25 = pygame.font.SysFont('Arial Black', 25)
font_orbitron_40 = pygame.font.SysFont('Orbitron', 40)
font_arial_black_50 = pygame.font.SysFont('Arial Black', 50)



# Gerer le 'menu principal'
# créer tous les textes
texte_nom_jeu = font_orbitron_40.render('Symmetry Dash', 1, (0, 0, 0)) # texte du nom du jeu
texte_jouer = font_arial_black_50.render('GO', 1, (0, 0, 0)) # texte du bouton permettant de lancer le jeu
texte_version_actuel = font_arial_black_15.render('V0.1 FRENCH', 1, (0, 0, 0)) # texte de la version actuel du jeu
texte_info_plus = font_arial_black_15.render('?', 1, (0, 0, 0))

# Fonction affichant les objets sur le menu principal
def menu_principal():
    # si la phase est la bonne
    if phase == 'Menu Principal':

        # couleur du BG
        screen.fill((255, 255, 255))
        # nom de la fenêtre
        pygame.display.set_caption(f'Symmetry Dash ({phase})')

        # afficher les boutons
        pygame.draw.rect(screen, (255, 165, 0), ((screen.get_width()-250)/2, 90, 250, 200), 0, 15) # bouton permettant de lancer le jeu
        pygame.draw.rect(screen, (0, 0, 255), (162, 190, 200, 180), 0, 15) # bouton permettant de changer de mode de jeu
        pygame.draw.rect(screen, (255, 0, 0), (screen.get_width()-20, screen.get_height()-20, 20, 20), 0, 4 ) # bouton permettant d'acceder au info plus

        # afficher les textes
        screen.blit(texte_nom_jeu, ((screen.get_width()-texte_nom_jeu.get_width())/2, 0)) # texte du nom du jeu
        screen.blit(texte_jouer, ((screen.get_width()-texte_jouer.get_width())/2, 90+(200-texte_jouer.get_height())/2)) # texte du bouton permettant de lancer le jeu
        screen.blit(texte_version_actuel, (0, screen.get_height()-texte_version_actuel.get_height()+4)) # texte de la version actuel du jeu
        screen.blit(texte_info_plus, (screen.get_width()-texte_info_plus.get_width()-4, screen.get_height()-texte_info_plus.get_height()+1)) # texte des infos bonus



# boucle du jeu
running = True
while running:
    # recuperer tous les evenements de la fenetre
    for event in pygame.event.get():
        # fermer la fenêtre
        if event.type == pygame.QUIT:
            running = False

    # recuperer la position de la souris
    pos = pygame.mouse.get_pos()

    # afficher le menu principal
    menu_principal()

    # mettre a jour la fenetre
    pygame.display.flip()

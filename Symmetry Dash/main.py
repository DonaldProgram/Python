import pygame
pygame.init()

# créer la fenetre
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Symmetry Dash')


# créer toutes les polices
font_15_arial_black = pygame.font.SysFont('Arial Black', 15)
font_40_arial_black = pygame.font.SysFont('Arial Black', 40)
font_45_arial_black = pygame.font.SysFont('Arial Black', 45)

# MENU PRINCIPAL
# raccourcis couleur
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
ORANGE = (255, 165, 0)
BLEU_CLAIR = (135, 206, 235)

# texte pas mis a jour
symmetry_dash_texte = font_45_arial_black.render('SYMMETRY DASH', 1, NOIR) # titre
version_actuel_texte = font_15_arial_black.render('V0.0 (only FRENCH)', 1, ROUGE) # bouton lancer

# fonction affichant le menu principal
def menu_principal():
    screen.fill(BLEU_CLAIR) # couleur du fond

    # créer les textes
    # bouton pour lancer le jeu
    bouton_play_texte = font_40_arial_black.render('>GO>', 1, NOIR) # texte du bouton lancer
    bouton_play_x = (1280 - bouton_play_texte.get_width()) / 2
    bouton_play_y = 100
    bouton_play_rect = pygame.Rect(bouton_play_x-10, bouton_play_y-10, bouton_play_texte.get_width()+20, bouton_play_texte.get_height()+20)

    if bouton_play_rect.collidepoint(pos): # si collision avec le bouton lancer
        bouton_play_texte = font_45_arial_black.render('>GO>', 1, NOIR)  # texte du bouton lancer
        bouton_play_x = (1280 - bouton_play_texte.get_width()) / 2
        bouton_play_rect.width += 20
        # bouton_play_rect.height += 20
        bouton_play_rect.x -= 10
        # bouton_play_rect.y -= 10

    # affichage texte
    screen.blit(symmetry_dash_texte, ((1280-symmetry_dash_texte.get_width())/2, 0)) # titre 'Symmetry Dash'
    screen.blit(version_actuel_texte, (0, 720-version_actuel_texte.get_height())) # version actuel du jeu

    pygame.draw.rect(screen, ORANGE, bouton_play_rect, 0, 10) # rectangle autour du bouton '<GO>'
    screen.blit(bouton_play_texte, (bouton_play_x, bouton_play_y)) # bouton '<GO>'


# boucle du jeu
running = True
while running:
    # recuperer tous les evenements du jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # recuperer la position de la souris
    pos = pygame.mouse.get_pos()

    # afficher le menu
    menu_principal()

    # mettre a jouer l'écran
    pygame.display.flip()

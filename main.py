import pygame
pygame.init()

# créer la fenetre
screen = pygame.display.set_mode((800, 900), pygame.RESIZABLE)
pygame.display.set_icon(pygame.image.load('Logo.jpg'))

# créer toutes les polices d'écriture
font = pygame.font.SysFont('Arial', 13)

# nom du fichier
nom_fichier = 'Sans Titre'



# Gerer ce que font tous les boutons du jeu

# créer tous les textes de la fenetre
x_bouton_rect = 0 # coordonné x des rects des boutons

# texte 'Fichier'
texte_fichier = font.render('Fichier', 1, (255, 255, 255))
texte_fichier_rect = texte_fichier.get_rect()
texte_fichier_rect.x = x_bouton_rect
x_bouton_rect += texte_fichier.get_width() + 5

# texte 'Edition'
texte_edition = font.render('Edition', 1, (255, 255, 255))
texte_edition_rect = texte_edition.get_rect()
texte_edition_rect.x = x_bouton_rect
x_bouton_rect += texte_edition.get_width() + 5

# texte 'Format'
texte_format = font.render('Format', 1, (255, 255, 255))
texte_format_rect = texte_format.get_rect()
texte_format_rect.x = x_bouton_rect
x_bouton_rect += texte_format.get_width() + 5

# texte 'Affichage'
texte_affichage = font.render('Affichage', 1, (255, 255, 255))
texte_affichage_rect = texte_affichage.get_rect()
texte_affichage_rect.x = x_bouton_rect
x_bouton_rect += texte_affichage.get_width() + 5

# texte 'Calendrier'
texte_calendrier = font.render('Calendrier', 1, (255, 255, 255))
texte_calendrier_rect = texte_calendrier.get_rect()
texte_calendrier_rect.x = x_bouton_rect
x_bouton_rect += texte_calendrier.get_width() + 5

# texte 'Aide'
texte_aide = font.render('Aide', 1, (255, 255, 255))
texte_aide_rect = texte_aide.get_rect()
texte_aide_rect.x = x_bouton_rect

# fonction servant a gerer tous les boutons du jeu
def bouton():
    # Afficher tous les textes des boutons
    for texte, rect in [(texte_fichier, texte_fichier_rect),
                       (texte_edition, texte_edition_rect),
                       (texte_format, texte_format_rect),
                       (texte_affichage, texte_affichage_rect),
                       (texte_calendrier, texte_calendrier_rect),
                       (texte_aide, texte_aide_rect)]:
        if rect.collidepoint(pos):
            pygame.draw.rect(screen, (0, 120, 215), rect)
        screen.blit(texte, rect.topleft)


# boucle du jeu
running = True
while running:
    # recuperer tous les evenements de la fenetre
    for event in pygame.event.get():
        # fermer la fenetre
        if event.type == pygame.QUIT:
            running = False

    # recuperer la position de la souris
    pos = pygame.mouse.get_pos()

    # couleur du BG
    screen.fill((30, 30, 30))

    # changer le nom de la fenetre
    pygame.display.set_caption(f'{nom_fichier} - Bloc-notes')

    # afficher tous les boutons a l'écran
    bouton()

    # mettre a jour la fenetre
    pygame.display.flip()

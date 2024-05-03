import pygame
pygame.init()

# créer la fenetre
screen = pygame.display.set_mode((800, 900), pygame.RESIZABLE)
pygame.display.set_icon(pygame.image.load('Logo.jpg'))

# créer toutes les polices d'écriture
font = pygame.font.SysFont('Arial', 13)

# nom du fichier
nom_fichier = 'Sans Titre'

# variable servant a savoir la phase en cours
phase = 'Bloc-notes-ecriture'

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
def bloc_notes_bouton():
    global phase

    # Afficher tous les textes des boutons
    for texte, rect in [(texte_fichier, texte_fichier_rect),
                       (texte_edition, texte_edition_rect),
                       (texte_format, texte_format_rect),
                       (texte_affichage, texte_affichage_rect),
                       (texte_calendrier, texte_calendrier_rect),
                       (texte_aide, texte_aide_rect)]:
        # si collision avec la souris
        if rect.collidepoint(pos):
            pygame.draw.rect(screen, (0, 120, 215), rect)
            # si clique sur un bouton
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect == texte_fichier_rect:
                        print('FICHIER')
                        phase = 'Bloc-notes-fichier'

                    elif rect == texte_edition_rect:
                        print('EDITION')
                        phase = 'Bloc-notes-edition'

                    elif rect == texte_format_rect:
                        print('FORMAT')
                        phase = 'Bloc-notes-format'

                    elif rect == texte_affichage_rect:
                        print('AFFICHAGE')
                        phase = 'Bloc-notes-affichage'

                    elif rect == texte_calendrier_rect:
                        print('CALENDRIER')
                        phase = 'Bloc-notes-calendrier'

                    elif rect == texte_aide_rect:
                        print('AIDE')
                        phase = 'Bloc-notes-aide'

        # afficher le bouton en haut de l'écran
        screen.blit(texte, rect.topleft)

    # afficher la delimitation entre les boutons et la zone de texte
    pygame.draw.rect(screen, (255, 255, 255), (0, texte_fichier.get_height()+1, screen.get_width(), 1))



# Gerer l'ecriture dans le Bloc-notes
liste_texte = []

# fonctions servant a gerer l'ecriture du texte dans le Bloc-notes
def bloc_notes_ecrire():
    global phase, liste_texte

    # créer le rect permettant de retourner en mode écriture
    rect_bloc_notes_ecriture = pygame.Rect((0, texte_fichier.get_height() + 2, screen.get_width(), screen.get_height()))
    # passer la phase en mode ecriture
    if rect_bloc_notes_ecriture.collidepoint(pos):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            phase = 'Bloc-notes-ecriture'


    if phase == 'Bloc-notes-ecriture':
        # ajouter les touches pressés au textes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(liste_texte) > 0:
                liste_texte.pop()
            if event.unicode.isprintable() and event.unicode != '':
                liste_texte.append(event.unicode)

# fonctions servant a gerer l'affichage du texte dans le Bloc-notes
dernier_temps = pygame.time.get_ticks()
curseur_visible = True
def bloc_notes_affichage():
    global dernier_temps, curseur_visible

    # afficher les textes a l'écran
    texte_bloc_notes_ecriture = ''.join(liste_texte)
    texte = font.render(texte_bloc_notes_ecriture, 1, (255, 255, 255))
    screen.blit(texte, (0, texte_fichier.get_height()+2))

    # afficher le curseur permettant de savoir ou on est entrain d'écrire
    temps_actuel = pygame.time.get_ticks()
    if temps_actuel-dernier_temps >= 500:
        curseur_visible = not curseur_visible
        dernier_temps = pygame.time.get_ticks()
    if curseur_visible:
        pygame.draw.rect(screen, (255, 255, 255), (texte.get_width(), texte_fichier.get_height()+4, 1, texte.get_height()-2))


# mettre le nb de FPS
clock = pygame.time.Clock()
# boucle du jeu
running = True
while running:

    # recuperer la position de la souris
    pos = pygame.mouse.get_pos()

    # couleur du BG
    screen.fill((30, 30, 30))

    # recuperer tous les evenements de la fenetre
    for event in pygame.event.get():
        # fermer la fenetre
        if event.type == pygame.QUIT:
            running = False

        # pouvoir écrire dans le Bloc-notes
        bloc_notes_ecrire()

    # afficher tous les boutons a l'écran
    bloc_notes_bouton()

    # afficher les textes a l'écran
    bloc_notes_affichage()


    # changer le nom de la fenetre
    pygame.display.set_caption(f'{nom_fichier} - Bloc-notes')

    # mettre le nb de FPS
    clock.tick(60)

    # mettre a jour la fenetre
    pygame.display.flip()

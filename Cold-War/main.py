import pygame, random
pygame.init()

# Créer la fenêtre
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Cold-WAR')


# Créer toutes les polices d'écriture
font_35 = pygame.font.SysFont('Arial', 35)
font_30 = pygame.font.SysFont('Arial', 30)
font_20 = pygame.font.SysFont('Arial', 20)
font_13 = pygame.font.SysFont('Arial', 13)


# Variable permettant de gerer les différantes phases du jeu
phase = 'Menu Principal'



# Créer le menu principal

# Créer tous les textes
menu_principal_texte_titre = font_35.render('COLD-WAR', 1, (255, 255, 255))
menu_principal_texte_lancer = font_35.render('Partir au combat !', 1, (255, 255, 255))
menu_principal_texte_parametre = font_35.render('Paramètres', 1, (255, 255, 255))
menu_principal_texte_version = font_13.render('V0.0', 1, (255, 255, 255))
menu_principal_texte_info_plus = font_13.render('?', 1, (0, 0, 0))

# Créer tous les rects des boutons
# bouton permettant de lancer le jeu
menu_principal_texte_lancer_rect = menu_principal_texte_lancer.get_rect()
menu_principal_texte_lancer_rect.x, menu_principal_texte_lancer_rect.y = (1280-menu_principal_texte_lancer.get_width())/2, 290

# bouton permettant de changer les paramètre
menu_principal_texte_parametre_rect = menu_principal_texte_parametre.get_rect()
menu_principal_texte_parametre_rect.x, menu_principal_texte_parametre_rect.y = (1280-menu_principal_texte_parametre.get_width())/2, 340

# créer les textes de décoration aléatoirement
menu_principal_liste_texte_aleatoire = ['THE SOUND OF FREEDOM.', 'THE TEST', 'THE BEST', 'THE CREATOR']
menu_principal_texte_aleatoire = menu_principal_liste_texte_aleatoire[random.randint(0, len(menu_principal_liste_texte_aleatoire)-1)]
menu_principal_texte_aleatoire = font_20.render(menu_principal_texte_aleatoire, 1, (255, 255, 0))
menu_principal_texte_aleatoire = pygame.transform.rotate(menu_principal_texte_aleatoire, 20)

# Fonction affichant le menu principal
def menu_principal():
    global phase, menu_principal_texte_lancer, menu_principal_texte_parametre

    # Si la phase est la bonne
    if phase == 'Menu Principal':

        # Mettre le BG de la fenetre
        screen.fill((30, 30, 30))

        # Afficher les rects de couleur representant la séparation entre USA et URSS
        # pygame.draw.rect(screen, (0, 0, 255), (0, 0, 300, 720))
        # pygame.draw.rect(screen, (255, 0, 0), (980, 0, 300, 720))


        # Afficher les textes a l'écran
        screen.blit(menu_principal_texte_titre, ((1280-menu_principal_texte_titre.get_width())/2, 20)) # nom du jeu
        screen.blit(menu_principal_texte_lancer, ((1280-menu_principal_texte_lancer.get_width())/2, 290)) # texte lancer le jeu
        screen.blit(menu_principal_texte_parametre, ((1280-menu_principal_texte_parametre.get_width())/2, 340)) # texte changer les paramètres
        screen.blit(menu_principal_texte_version, (0, screen.get_height()-menu_principal_texte_version.get_height())) # version actuelle
        # screen.blit(menu_principal_texte_info_plus, (1280-menu_principal_texte_info_plus.get_width()-5, 720-menu_principal_texte_info_plus.get_height()-5)) # info plus
        # screen.blit(menu_principal_texte_aleatoire, ((300-menu_principal_texte_aleatoire.get_width())/2, 315)) # texte aleatoire décoration

        # Si collision avec les boutons
        # bouton lancer
        if menu_principal_texte_lancer_rect.collidepoint(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    phase = 'Jeu'

        # changer la couleur du texte si touché par la souris
            menu_principal_texte_lancer = font_35.render('[Partir au combat !]', 1, (255, 255, 0))
        else:
            menu_principal_texte_lancer = font_35.render('Partir au combat !', 1, (255, 255, 255))

        # bouton paramètre
        if menu_principal_texte_parametre_rect.collidepoint(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    phase = 'Paramètre'

        # changer la couleur du texte si touché par la souris
            menu_principal_texte_parametre = font_35.render('[Paramètres]', 1, (255, 255, 0))
        else:
            menu_principal_texte_parametre = font_35.render('Paramètres', 1, (255, 255, 255))

        # bouton info plus
        # REPRENDRE ICI, CHANGER LES DIMENSIONS DU RECT :)
        # changer les coordonnés du rect info plus
        pygame.draw.rect(screen, (255, 255, 255), (1269, 706, 11, 14))
        screen.blit(menu_principal_texte_info_plus, (1280-menu_principal_texte_info_plus.get_width()-2, 720-menu_principal_texte_info_plus.get_height()+1)) # texte info plus



# Créer le Jeu

# Class permettant de créer les joueurs
class Joueur:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur
        self.chargeur = 10

    # methode permettant d'afficher les joueurs
    def afficher_joueur(self):
        pygame.draw.rect(screen, self.couleur, (self.x, self.y, 15, 90))

    # afficher l'ATH
    def afficher_ATH(self):
        # joueur 1
        if self == joueur1:
            self.chargeur_texte = font_13.render(f'Joueur 1 : {self.chargeur}', 1, (0, 0, 255))
            screen.blit(self.chargeur_texte, (300, 300))
        # joueur 2
        else:
            self.chargeur_texte = font_13.render(f'Joueur 2 : {self.chargeur}', 1, (255, 0, 0))
            screen.blit(self.chargeur_texte, (400, 300))

# créer les joueurs
joueur1 = Joueur(10, 200, (0, 0, 255))
joueur2 = Joueur(200, 200, (255, 0, 0))

# Fonction affichant le Jeu
def Jeu():

    # Si la phase est la bonne
    if phase == 'Jeu':

        # Mettre le BG de la fenêtre
        screen.fill((30, 30, 30))

        # Gerer les joueurs
        # afficher les joueurs
        joueur1.afficher_joueur()
        joueur2.afficher_joueur()
        # joueur1.afficher_ATH()
        # joueur2.afficher_ATH()

        # deplacer les joueurs
        # joueur 1
        if pressed[pygame.K_z]:
            joueur1.y -= 7
        if pressed[pygame.K_s]:
            joueur1.y += 7
        # joueur 2
        if pressed[pygame.K_UP]:
            joueur2.y -= 7
        if pressed[pygame.K_DOWN]:
            joueur2.y += 7



# Variable permettant d'initialiser un certain nombre de FPS
clock = pygame.time.Clock()

# Variable permettant de detecter quand un clic a lieu
clic = None

# Boucle du jeu
running = True
while running:
    # Recuperer tous les evenements de la fenetre
    for event in pygame.event.get():
        # fermer la fenetre
        if event.type == pygame.QUIT:
            running = False

    # recuperer les touches pressés
    pressed = pygame.key.get_pressed()

    # Recuperer la position de la souris
    pos = pygame.mouse.get_pos()


    # Afficher le menu principal
    menu_principal()

    # Afficher le menu principal
    Jeu()

    # Initialiser le nombre de FPS
    clock.tick(60)

    # Mettre a jour la fenetre
    pygame.display.flip()

pygame.quit()

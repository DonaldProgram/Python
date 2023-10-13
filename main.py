# import de tous les modules
from sprites import *
import pygame
pygame.init()
#...

# parametre de la fenetre
screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.RESIZABLE | pygame.FULLSCREEN)
pygame.display.set_caption("Que du bloc")
pygame.display.set_icon(Player.Joueur_1)
#...












# creer la map (Pierres_cuites)
def Map_Pierres_cuites():
    x_Pierres_cuites = 0
    y_Pierres_cuites = -40
    while y_Pierres_cuites < screen.get_height():
        while x_Pierres_cuites < screen.get_width():
            screen.blit(Bloc.Pierres_cuites, (x_Pierres_cuites, y_Pierres_cuites))
            x_Pierres_cuites += 48
        x_Pierres_cuites = 0
        y_Pierres_cuites += 48
#...





# creer le menu de début du jeu
def Menu():
    screen.blit(Texte.Titre_Minecraft, (500, 100))
#...





# creer le déplacement du joueur joueur
x_joueur = 24
y_joueur = 24
vitesse_joueur = 8
def Joueur():
    global x_joueur, y_joueur

    if y_joueur > 0:
        if pressed[pygame.K_z]:
            y_joueur -= vitesse_joueur
    if y_joueur < screen.get_height()-Player.Joueur_1.get_height():
        if pressed[pygame.K_s]:
            y_joueur += vitesse_joueur
    if x_joueur > 0:
        if pressed[pygame.K_q]:
            x_joueur -= vitesse_joueur
    if x_joueur < screen.get_width()-Player.Joueur_1.get_width():
        if pressed[pygame.K_d]:
            x_joueur += vitesse_joueur

    screen.blit(Player.Joueur_1, (x_joueur, y_joueur))
#...












# boucle du jeu
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE|pygame.FULLSCREEN)


    # recuperer toutes les touches pressées
    pressed = pygame.key.get_pressed()
    #...

    # fonction du jeu
    Map_Pierres_cuites()
    Menu()
    Joueur()
    #...

    clock.tick(60)
    pygame.display.flip()
#...
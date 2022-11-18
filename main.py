# importation du module pygame + initialisation de tout ses modules
import pygame
pygame.init()

# creation de la fenetre + changement du titre + du logo
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("QUIZZ DRAPEAU")
ICON = pygame.image.load("decoration/philippeGardas.png")
pygame.display.set_icon(ICON)

# variable qui fera tourner la fenetre qui affichera le menu
fenetreMENU = True

# variable servant a afficher le mots 
police = pygame.font.SysFont("monospace", 60)
Menu_texte = police.render("MENU", 1, (0, 0, 0))
police = pygame.font.SysFont("monospace", 30)
Entré_Debut_texte = police.render("Appuyer sur entrer", 1, (0, 0, 0))
Entré_Fin_texte = police.render("pour lancer le jeu", 1, (0, 0, 0))


# Charge toutes les images de decoration
arbreSimple = pygame.image.load("decoration/arbre.png")
soleil = pygame.image.load("decoration/soleil.png")
arbreMultiple = pygame.image.load("decoration/forets.png")
arbreNeige = pygame.image.load("decoration/arbreHiver.png")
maisonNeige = pygame.image.load("decoration/maisonNeige.png")
nuageNeige = pygame.image.load("decoration/nuageNeige.png")
neige = pygame.image.load("decoration/neige.png")
nuage = pygame.image.load("decoration/nuages.png")
tracteur = pygame.image.load("decoration/tracteur.png")
ble = pygame.image.load("decoration/blé.png")
lutin = pygame.image.load("decoration/lutin1.png")
bouton = pygame.image.load("decoration/bouton.png")

# rectangle du bouton
rectBoutonDebut = bouton.get_rect() 
rectBoutonDebut.x = 500
rectBoutonDebut.y = 200

# boucle gerant tous ce qui se passe dans la fenetre du menu
while fenetreMENU:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fenetreMENU = False
            pygame.quit()

    # fonction pour lancer le jeu a partir du bouton
        pos = pygame.mouse.get_pos()
        if rectBoutonDebut.collidepoint(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                fenetreMENU = False

    # couleur de l'arriere plan = blanc
    screen.fill("#e4faff")
    
    # ajout des decoration:

    # ajout du mots menu
    screen.blit(Menu_texte, (315, 0))

    # affichage du logo PG
    screen.blit(ICON, (0, -5))
    
    # affichage du soleil
    screen.blit(soleil, (650, 0))
    
    # affichage de l'arbre simple
    screen.blit(arbreSimple, (0, 476))
    
    # affichage de l'arbre enneigé
    screen.blit(arbreNeige, (230, 475))
   
    # affichage de la maison
    screen.blit(maisonNeige, (120, 476))

    # affichage de plusieurs nuages simple
    screen.blit(nuage, (0, 100))
    screen.blit(nuage, (180, 150))

    # affichage de flocons de neige 
    screen.blit(neige, (0, 250))
    screen.blit(neige, (180, 300))

    # affichage du blé 
    screen.blit(ble, (580, 490))

    # affichage du tracteur
    screen.blit(tracteur, (580, 510))

    # affichage du lutin1
    screen.blit(lutin, (375, 472))

    # affichage du bouton pour lancer le jeu
    screen.blit(bouton, (rectBoutonDebut))

    # mise a jour de l'ecran
    pygame.display.flip()
# importation du module pygame + initialisation de tout ses modules
import pygame
pygame.init()

# creation de la fenetre + changement du titre + du logo
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("QUIZZ DRAPEAU")
ICON = pygame.image.load("decoration/philippeGardas.png")
pygame.display.set_icon(ICON)

# Charge toutes les images de decoration
class Decoration():
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
    boutonReponse1 = pygame.image.load("decoration/rectangle.png")
    boutonReponse2 = pygame.image.load("decoration/rectangle.png")
    boutonReponse3 = pygame.image.load("decoration/rectangle.png")
    boutonReponse4 = pygame.image.load("decoration/rectangle.png")

# charge toute les images de drapeaux
class DrapeauImage():
    allemagne = pygame.image.load("drapeau/allemagne.png")

# boucle running faisant tourner le jeu tant que la croix n'a pas ete pressé
running = True




# fonction gerant le menu
# rectangle du bouton
rectBoutonStart = Decoration.bouton.get_rect() 
rectBoutonStart.x = 500
rectBoutonStart.y = 200
# variable faisant tourner le menu
fenetreMenu = True
# fonction du menu
def Menu():
    global fenetreMenu
    if fenetreMenu == True:  
        # fonction pour lancer le jeu a partir du bouton
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectBoutonStart.collidepoint(pos):
                    return True
                    fenetreMenu = False
                else:
                    return False

        # variable servant a afficher le mots MENU
        police = pygame.font.SysFont("monospace", 60)
        Menu_texte = police.render("MENU", 1, (0, 0, 0))
        
        # couleur de l'arriere plan = blanc
        screen.fill("#e4faff")
        
        # ajout des decoration:
        # ajout du mots menu
        screen.blit(Menu_texte, (315, 0))

        # affichage du logo PG
        screen.blit(ICON, (0, -5))
        
        # affichage du soleil
        screen.blit(Decoration.soleil, (650, 0))
        
        # affichage de l'arbre simple
        screen.blit(Decoration.arbreSimple, (0, 476))
        
        # affichage de l'arbre enneigé
        screen.blit(Decoration.arbreNeige, (230, 475))

        # affichage de la maison
        screen.blit(Decoration.maisonNeige, (120, 476))

        # affichage de plusieurs nuages simple
        screen.blit(Decoration.nuage, (0, 100))
        screen.blit(Decoration.nuage, (180, 150))

        # affichage de flocons de neige 
        screen.blit(Decoration.neige, (0, 250))
        screen.blit(Decoration.neige, (180, 300))

        # affichage du blé 
        screen.blit(Decoration.ble, (580, 490))

        # affichage du tracteur
        screen.blit(Decoration.tracteur, (580, 510))

        # affichage du lutin1
        screen.blit(Decoration.lutin, (375, 472))

        # affichage du bouton pour lancer le jeu
        screen.blit(Decoration.bouton, (rectBoutonStart))




# rectangle des reponses
rectBoutonrep1 = Decoration.boutonReponse1.get_rect() 
rectBoutonrep1.x = 30
rectBoutonrep1.y = 160

rectBoutonrep2 = Decoration.boutonReponse2.get_rect() 
rectBoutonrep2.x = 30
rectBoutonrep2.y = 210

rectBoutonrep3 = Decoration.boutonReponse3.get_rect() 
rectBoutonrep3.x = 30
rectBoutonrep3.y = 260

rectBoutonrep4 = Decoration.boutonReponse4.get_rect() 
rectBoutonrep4.x = 30
rectBoutonrep4.y = 310
# fonction qui fait tourner le quizz
def Drapeaux():
    if fenetreDrapeau == True:
        # variable servant a afficher le mots quizz
        police = pygame.font.SysFont("monospace", 60)
        QUIZ_texte = police.render("QUIZZ", 1, (0, 0, 0))

        # affichage du mots quizz
        screen.blit(QUIZ_texte, (300, 0))
        
        # affichage du mots choisissez une reponse
        police = pygame.font.SysFont(".", 40)
        Choose_reponse1 = police.render("Choisissez", 1, (0, 0, 0))
        Choose_reponse2 = police.render("votre reponse:", 1, (0, 0, 0))
        screen.blit(Choose_reponse1, (20, 140))
        screen.blit(Choose_reponse2, (20, 165))

        # afficher le drapeaux test allemagne
        screen.blit(DrapeauImage.allemagne, (330, 100))

        # afficher les rectangle de reponse
        screen.blit(Decoration.boutonReponse1, rectBoutonrep1)
        screen.blit(Decoration.boutonReponse2, rectBoutonrep2)
        screen.blit(Decoration.boutonReponse3, rectBoutonrep3)
        screen.blit(Decoration.boutonReponse4, rectBoutonrep4)
        



# boucle de toute les fenetres après le menu
fenetreDrapeau = False
# boucle du jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    if Menu() == True:
        fenetreDrapeau = True
    else:
        Menu()
 
    if fenetreDrapeau == True:
        screen.fill("#e4faff")
        Drapeaux()
        # appeler la fonction drapeau

    # mise a jour de l'ecran
    pygame.display.flip()

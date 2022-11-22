# importation du module pygame et random et time + initialisation de tout ses modules
import pygame, random, time
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
    boutonReponseJuste = pygame.image.load("decoration/rectangle.png")
    boutonReponse2 = pygame.image.load("decoration/rectangle.png")
    boutonReponse3 = pygame.image.load("decoration/rectangle.png")
    boutonReponse4 = pygame.image.load("decoration/rectangle.png")
    perenoel = pygame.image.load("decoration/perenoel.png")
    guirlande = pygame.image.load("decoration/guirlande1.png")
    guirlande2 = pygame.image.load("decoration/guirlande2.png")
    cookie = pygame.image.load("decoration/cookie.png")
    renne = pygame.image.load("decoration/renne.png")
    DECOallemagne = pygame.image.load("decoration/allemagneDECO.png")
    DECOcasqueallemagne = pygame.image.load("decoration/casqueDECO.png")
    DECOterreAllemagne = pygame.image.load("decoration/DECOguerreMondial.png")
    DECOsoldatAllemagne = pygame.image.load("decoration/soldats.png")
    pouceJUSTE = pygame.image.load("decoration/pouceJUSTE.png")
    plus1point = pygame.image.load("decoration/plus1point.png")
    clinDoeil = pygame.image.load("decoration/clin-doeil.png")
    cool = pygame.image.load("decoration/cool.png")
    fou = pygame.image.load("decoration/fou.png")
    heureux = pygame.image.load("decoration/heureux.png")
    ia = pygame.image.load("decoration/ia.png")
    illuminati = pygame.image.load("decoration/illuminati.png")
    muscle = pygame.image.load("decoration/muscle.png")
    prorammation = pygame.image.load("decoration/programmation.png")
    serein = pygame.image.load("decoration/serein.png")
    pouceFAUX = pygame.image.load("decoration/pouceFAUX.png")
    triste1 = pygame.image.load("decoration/triste1.png")
    triste2 = pygame.image.load("decoration/triste2.png")
    triste3 = pygame.image.load("decoration/triste3.png")
    triste4 = pygame.image.load("decoration/triste4.png")
    triste5 = pygame.image.load("decoration/triste5.png")


# ajout de la variable score
score = 0
policeScore = pygame.font.SysFont("MONOSPACE", 35)
texteScore = policeScore.render("SCORE:" + str(score), 1, (0, 0, 0))

# charge toute les images de drapeaux
class DrapeauImage():
    allemagne = pygame.image.load("drapeau/allemagne.png")
    anglais = pygame.image.load("drapeau/anglais.png")
    australie = pygame.image.load("drapeau/australie.png")
    bresil = pygame.image.load("drapeau/bresil.png")
    canada = pygame.image.load("drapeau/canada.png")
    chine = pygame.image.load("drapeau/chine.png")
    danemark = pygame.image.load("drapeau/danemark.png")
    espagne = pygame.image.load("drapeau/espagne.png")
    france = pygame.image.load("drapeau/france.png")
    UE = pygame.image.load("drapeau/UE.png")
    USA = pygame.image.load("drapeau/USA.png")
    italie = pygame.image.load("drapeau/italie.png")
    japon = pygame.image.load("drapeau/japon.png")
    maroc = pygame.image.load("drapeau/maroc.png")
    norvege = pygame.image.load("drapeau/norvege.png")
    pologne = pygame.image.load("drapeau/pologne.png")
    portugal = pygame.image.load("drapeau/portugal.png")
    russie = pygame.image.load("drapeau/russie.png")
    senegale = pygame.image.load('drapeau/senegale.png')
    suede = pygame.image.load("drapeau/suede.png")
    suisse = pygame.image.load("drapeau/suisse.png")
    tunisie = pygame.image.load("drapeau/tunisie.png")
    turquie = pygame.image.load("drapeau/turquie.png")

# liste pour afficher les drapeaux a la suite
numeroPAYS = 0
listePAYS = [DrapeauImage.allemagne, DrapeauImage.anglais, DrapeauImage.australie, DrapeauImage.bresil, DrapeauImage.canada, DrapeauImage.chine, DrapeauImage.danemark, DrapeauImage.espagne, DrapeauImage.france, DrapeauImage.UE, DrapeauImage.USA, DrapeauImage.italie, DrapeauImage.japon, DrapeauImage.maroc, DrapeauImage.norvege, DrapeauImage.pologne, DrapeauImage.portugal, DrapeauImage.russie, DrapeauImage.senegale, DrapeauImage.suede, DrapeauImage.suisse, DrapeauImage.tunisie, DrapeauImage.turquie]

listeREPjuste = ["Allemagne", "Anglais", "Australie", "Bresil", "Canada", "Chine", "Danemark", "Espagne", "France", "Unions E", "Etats Unis", "Italie", "Japon", "Maroc", "Norvege", "Pologne", "Portugal", "Russie", "Senegale", "Suede", "Suisse", "Tunisie", "Turquie"]
listeREPfaux1 = ["Italie", "Unions E", "Senegale", "Portugal", "Suede", "Japon", "Canada"]
listeREPfaux2 = ["Etats-Unis", "Danemark", "Pologne", "Otan", "Norvege", "Taiwan", "Norvege"]
listeREPfaux3 = ["Belgique", "Norvege", "Tunisie", "Chine", "Pologne", "Tunisie", "Suede"]

# variable running faisant tourner le jeu tant que la croix n'a pas ete pressé
running = True



# fonction gerant le menu
# rectangle du bouton
rectBoutonStart = Decoration.bouton.get_rect() 
rectBoutonStart.x = 465
rectBoutonStart.y = 0
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

        # affichage des guirlande
        screen.blit(Decoration.guirlande, (470, 110))
        screen.blit(Decoration.guirlande2, (320, 10))

        # affichage de cookie
        screen.blit(Decoration.cookie, (675, 300))

        # affichage d'un renne
        screen.blit(Decoration.renne, (350, 230))

        # affichage du perenoel
        screen.blit(Decoration.perenoel, (370, 235))




# rectangle des reponses + choix aleatoire de leurs emplacements
choix_reponse_bouton = [20, 170, 490, 640]

# choix aleatoire de leurs emplacement
rectBoutonrepJuste = Decoration.boutonReponseJuste.get_rect()
rectBoutonrepJuste.x = random.choice(choix_reponse_bouton)
choix_reponse_bouton.remove(rectBoutonrepJuste.x)
rectBoutonrepJuste.y = 200

rectBoutonrep2 = Decoration.boutonReponseJuste.get_rect()
rectBoutonrep2.x = random.choice(choix_reponse_bouton)
choix_reponse_bouton.remove(rectBoutonrep2.x)
rectBoutonrep2.y = 200

rectBoutonrep3 = Decoration.boutonReponseJuste.get_rect()
rectBoutonrep3.x = random.choice(choix_reponse_bouton)
choix_reponse_bouton.remove(rectBoutonrep3.x)
rectBoutonrep3.y = 200

rectBoutonrep4 = Decoration.boutonReponseJuste.get_rect()
rectBoutonrep4.x = random.choice(choix_reponse_bouton)
choix_reponse_bouton.remove(rectBoutonrep4.x)
rectBoutonrep4.y = 200

# fonction qui fait tourner le quizz
def Drapeaux():
    global fenetreDrapeau, score, texteScore, numeroPAYS, rectBoutonrepJuste, rectBoutonrep2, rectBoutonrep3, rectBoutonrep4
    # affichage du score + mise a jour du score
    texteScore = policeScore.render("SCORE:" + str(score), 1, (0, 0, 0))
    screen.blit(texteScore, (630, 0))
    
    if fenetreDrapeau == True:
        # verifer si un des rectangle de reponses est cliquer
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectBoutonrepJuste.collidepoint(pos):
                    REPjuste()
                elif rectBoutonrep2.collidepoint(pos):
                    REPfausse()
                elif rectBoutonrep3.collidepoint(pos):
                    REPfausse()
                elif rectBoutonrep4.collidepoint(pos):
                    REPfausse()

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
       
        # afficher les rectangle de reponse
        screen.blit(Decoration.boutonReponseJuste, rectBoutonrepJuste)
        screen.blit(Decoration.boutonReponse2, rectBoutonrep2)
        screen.blit(Decoration.boutonReponse3, rectBoutonrep3)
        screen.blit(Decoration.boutonReponse4, rectBoutonrep4)
      
        # afficher les drapeaux 
        screen.blit(listePAYS[numeroPAYS], (330, 100))

        # afficher les textes sur les rectangles
        police = pygame.font.SysFont("monospace", 20)
        reponse_texte1 = police.render(listeREPjuste[numeroPAYS], 1, (0, 255, 255))
        screen.blit(reponse_texte1, (rectBoutonrepJuste.x+9, rectBoutonrepJuste.y + 54))
        reponse_texte2 = police.render("Etats-Unis", 1, (0, 255, 255))
        screen.blit(reponse_texte2, (rectBoutonrep2.x + 6, rectBoutonrep2.y + 54))
        reponse_texte3 = police.render("Belgique", 1, (0, 255, 255))
        screen.blit(reponse_texte3, (rectBoutonrep3.x + 15, rectBoutonrep3.y + 54))
        reponse_texte4 = police.render("Italie", 1, (0, 255, 255))
        screen.blit(reponse_texte4, (rectBoutonrep4.x + 23, rectBoutonrep4.y + 54))

        # decoration de la fenetre
        screen.blit(Decoration.DECOallemagne, (500, 350))
        screen.blit(Decoration.DECOcasqueallemagne, (0, 450))
        screen.blit(Decoration.DECOterreAllemagne, (230, 400))
        screen.blit(Decoration.DECOsoldatAllemagne, (630, 460))


# creer la fenetre pour que si le joueur clique sur la bonne reponse sa affiche une nouvelle fenetre
def REPjuste():
    global score, numeroPAYS, rectBoutonrepJuste, rectBoutonrep2, rectBoutonrep3, rectBoutonrep4
    score += 1
    policeScore = pygame.font.SysFont("MONOSPACE", 35)
    texteScore = policeScore.render("SCORE:" + str(score), 1, (0, 0, 0))
    screen.fill((0, 255, 255))
    screen.blit(texteScore, (630, 0))
    screen.blit(Decoration.pouceJUSTE, (150, 90))
    screen.blit(Decoration.plus1point, (600, 0))
    screen.blit(Decoration.clinDoeil, (20, 0))
    screen.blit(Decoration.cool, (120, 20))
    screen.blit(Decoration.fou, (45, 150))
    screen.blit(Decoration.heureux, (0, 250))
    screen.blit(Decoration.ia, (85, 285))
    screen.blit(Decoration.illuminati, (360, 0))
    screen.blit(Decoration.muscle, (700, 200))
    screen.blit(Decoration.prorammation, (620, 460))
    screen.blit(Decoration.serein, (650, 390))

    pygame.display.flip()
    time.sleep(3)

    # rectangle des reponses + choix aleatoire de leurs emplacements
    choix_reponse_bouton = [20, 170, 490, 640]

    # choix aleatoire de leurs emplacement
    rectBoutonrepJuste = Decoration.boutonReponseJuste.get_rect()
    rectBoutonrepJuste.x = random.choice(choix_reponse_bouton)
    choix_reponse_bouton.remove(rectBoutonrepJuste.x)
    rectBoutonrepJuste.y = 200

    rectBoutonrep2 = Decoration.boutonReponseJuste.get_rect()
    rectBoutonrep2.x = random.choice(choix_reponse_bouton)
    choix_reponse_bouton.remove(rectBoutonrep2.x)
    rectBoutonrep2.y = 200

    rectBoutonrep3 = Decoration.boutonReponseJuste.get_rect()
    rectBoutonrep3.x = random.choice(choix_reponse_bouton)
    choix_reponse_bouton.remove(rectBoutonrep3.x)
    rectBoutonrep3.y = 200

    rectBoutonrep4 = Decoration.boutonReponseJuste.get_rect()
    rectBoutonrep4.x = random.choice(choix_reponse_bouton)
    choix_reponse_bouton.remove(rectBoutonrep4.x)
    rectBoutonrep4.y = 200    


    # afficher les textes sur les rectangles
    police = pygame.font.SysFont("monospace", 20)
    reponse_texte1 = police.render(listeREPjuste[numeroPAYS], 1, (0, 255, 255))
    screen.blit(reponse_texte1, (rectBoutonrepJuste.x+9, rectBoutonrepJuste.y + 54))
    reponse_texte2 = police.render("Etats-Unis", 1, (0, 255, 255))
    screen.blit(reponse_texte2, (rectBoutonrep2.x + 6, rectBoutonrep2.y + 54))
    reponse_texte3 = police.render("Belgique", 1, (0, 255, 255))
    screen.blit(reponse_texte3, (rectBoutonrep3.x + 15, rectBoutonrep3.y + 54))
    reponse_texte4 = police.render("Italie", 1, (0, 255, 255))
    screen.blit(reponse_texte4, (rectBoutonrep4.x + 23, rectBoutonrep4.y + 54))

    numeroPAYS += 1
    

# creer la fenetre pour que si le joueur clique sur la mauvaise reponse sa affiche une nouvelle fenetre
def REPfausse():
    global numeroPAYS, rectBoutonrepJuste, rectBoutonrep2, rectBoutonrep3, rectBoutonrep4
    policeScore = pygame.font.SysFont("MONOSPACE", 35)
    texteScore = policeScore.render("SCORE:" + str(score), 1, (0, 0, 0))
    screen.fill((150, 0, 150))
    screen.blit(texteScore, (630, 0))
    screen.blit(Decoration.pouceFAUX, (150, 50))
    screen.blit(Decoration.triste1, (250, 0))
    screen.blit(Decoration.triste2, (150, 180))
    screen.blit(Decoration.triste3, (70, 450))
    screen.blit(Decoration.triste4, (150, 400))
    screen.blit(Decoration.triste5, (660, 250))
    screen.blit(Decoration.triste1, (700, 10))
    screen.blit(Decoration.triste2, (200, 700))
    screen.blit(Decoration.triste3, (740, 180))
    screen.blit(Decoration.triste4, (680, 350))
    screen.blit(Decoration.triste5, (20, 0))

    pygame.display.flip()
    time.sleep(3)

    # rectangle des reponses + choix aleatoire de leurs emplacements
    choix_reponse_bouton = [20, 170, 490, 640]

    # choix aleatoire de leurs emplacement
    rectBoutonrepJuste = Decoration.boutonReponseJuste.get_rect()
    rectBoutonrepJuste.x = random.choice(choix_reponse_bouton)
    choix_reponse_bouton.remove(rectBoutonrepJuste.x)
    rectBoutonrepJuste.y = 200

    rectBoutonrep2 = Decoration.boutonReponseJuste.get_rect()
    rectBoutonrep2.x = random.choice(choix_reponse_bouton)
    choix_reponse_bouton.remove(rectBoutonrep2.x)
    rectBoutonrep2.y = 200

    rectBoutonrep3 = Decoration.boutonReponseJuste.get_rect()
    rectBoutonrep3.x = random.choice(choix_reponse_bouton)
    choix_reponse_bouton.remove(rectBoutonrep3.x)
    rectBoutonrep3.y = 200

    rectBoutonrep4 = Decoration.boutonReponseJuste.get_rect()
    rectBoutonrep4.x = random.choice(choix_reponse_bouton)
    choix_reponse_bouton.remove(rectBoutonrep4.x)
    rectBoutonrep4.y = 200

    # afficher les textes sur les rectangles
    police = pygame.font.SysFont("monospace", 20)
    reponse_texte1 = police.render(listeREPjuste[numeroPAYS], 1, (0, 255, 255))
    screen.blit(reponse_texte1, (rectBoutonrepJuste.x+9, rectBoutonrepJuste.y + 54))
    reponse_texte2 = police.render("Etats-Unis", 1, (0, 255, 255))
    screen.blit(reponse_texte2, (rectBoutonrep2.x + 6, rectBoutonrep2.y + 54))
    reponse_texte3 = police.render("Belgique", 1, (0, 255, 255))
    screen.blit(reponse_texte3, (rectBoutonrep3.x + 15, rectBoutonrep3.y + 54))
    reponse_texte4 = police.render("Italie", 1, (0, 255, 255))
    screen.blit(reponse_texte4, (rectBoutonrep4.x + 23, rectBoutonrep4.y + 54))

    numeroPAYS += 1


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
        pos = pygame.mouse.get_pos()
        Drapeaux()
        # appeler la fonction drapeau

    # mise a jour de l'ecran
    pygame.display.flip()

import pygame, random
pygame.init()

# création de la fenêtre
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('COLD-WAR')
# ...


# importer les son
son_shoot = pygame.mixer.Sound('song_shoot.wav')
son_touch = pygame.mixer.Sound('song_touch.wav')
son_musique = pygame.mixer.Sound("musique.wav")

son_musique.set_volume(0.3)
#...

# creer des canaux pour pouvoir mettre plusieur son a la fois
canal_son_shoot = pygame.mixer.Channel(1)
canal_son_touch = pygame.mixer.Channel(2)
#...


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

# definir une variable delay pour patienter un peu
delay = 200
delay_reclick = 1000  # Temps d'attente en millisecondes avant de pouvoir recliquer
#...

# fonction pour gérer le menu
choixOnglet = 'MenuMenu'
def Menu():
    global texte_jouer, texte_miroir, texte_parametre, choixMenu, last_change, choixOnglet, last_click_time
    pressed = pygame.key.get_pressed()

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
        current_time = pygame.time.get_ticks()
        if current_time - last_click_time < delay_reclick:
            return
        choixOnglet = 'MenuJouer'
        last_click_time = current_time
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
    global choixPartie, texte_1c1, texte_jouer, last_change, choixOnglet, last_click_time
    pressed = pygame.key.get_pressed()
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

    # vérifier si la touche Entrée est pressée
    if pressed[pygame.K_RETURN] and choixPartie == 1:
        current_time = pygame.time.get_ticks()
        if current_time - last_click_time < delay_reclick-300:
            return
        choixOnglet = 'MenuChoixPartie'
        last_click_time = current_time
    #...
#...




# fonction qui gere les bonus
# liste pour gerer les differant bonus qui doivent etre afficher
bonus = []
#...

current_time = 0

def Bonus():
    global current_time

    temps_ecoule = pygame.time.get_ticks()-current_time 

    # gerer si un bonus dois s'afficher
    if len(bonus) < 10:
        if temps_ecoule >= 12000:
            # ajouter des coordonné aleatoire au spawn de la balle bonus
            bonus.append((random.randint(200, 1700), random.randint(100, 900)))
            #...
            current_time = pygame.time.get_ticks()
    #...

    # afficher les bonus
    for bonuss in range(len(bonus)):
        pygame.draw.circle(screen, (0, 255, 0), (bonus[bonuss]), 40)
    #...
#...






# fonction gerant le 1c1
joueur1 = pygame.Surface((22, 130))
joueur1.fill((0, 0, 255))

joueur2 = pygame.Surface((22, 130))
joueur2.fill((255, 0, 0))

y1 = 540-joueur1.get_height()
y2 = 540-joueur2.get_height()

cooBalle1 = []
cooBalle2 = []

# var pour le temps d'attente entre chaque tir
delay_balle = 140

last_balle_time1 = 0
last_balle_time2 = 0
#...

# var pour les chargeurs des joueurs
chargeur1 = 10
chargeur2 = 10
#...

# gerer l'affichage des petites flash lorsque un joueur est touché
flashJoueur1 = pygame.Surface((1920, 1080), pygame.SRCALPHA)
flashJoueur1.fill((0, 0, 255, 110))

flashJoueur2 = pygame.Surface((1920, 1080), pygame.SRCALPHA)
flashJoueur2.fill((255, 0, 0, 140))
#...

v1lancer = False

point_joueur_1 = 0
point_joueur_2 = 0

def v1():
    global y1, y2, last_balle_time1, last_balle_time2, chargeur1, chargeur2, point_joueur_1, point_joueur_2, v1lancer
    current_time = pygame.time.get_ticks()



    # gerer le temps d'attente avant le 1v1
    if v1lancer == False:
        # afficher les deux joueur lors du temps d'attente
        screen.blit(joueur1, (15, y1))
        screen.blit(joueur2, (1882, y2))
        pygame.display.flip()
        #... 

        # afficher le compteur lors du temps d'attente
        # compteur 3
        font = pygame.font.SysFont(None, 200)
        text1 = font.render("3", True, (255, 255, 255))
        screen.blit(text1, ((1920-text1.get_width())/2, (1080-text1.get_height())/2-300))
        screen.blit(joueur1, (15, y1))
        screen.blit(joueur2, (1882, y2))
        pygame.display.flip()
        #...

        # compteur 2
        pygame.time.wait(1000)
        text1 = font.render("2", True, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(text1, ((1920-text1.get_width())/2, (1080-text1.get_height())/2-300))
        screen.blit(joueur1, (15, y1))
        screen.blit(joueur2, (1882, y2))
        pygame.display.flip()  
        #...

        # compteur 1
        pygame.time.wait(1000)
        text1 = font.render("1", True, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(text1, ((1920-text1.get_width())/2, (1080-text1.get_height())/2-300))
        screen.blit(joueur1, (15, y1))
        screen.blit(joueur2, (1882, y2))
        pygame.display.flip()
        pygame.time.wait(1000)
        #...

        # goooo
        text1 = font.render("GO !!", True, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(text1, ((1920-text1.get_width())/2, (1080-text1.get_height())/2-300))
        screen.blit(joueur1, (15, y1))
        screen.blit(joueur2, (1882, y2))
        pygame.display.flip()
        pygame.time.wait(1000)
        #...


        pygame.event.pump()
        pressed = pygame.key.get_pressed()
        v1lancer = True
    #...




    # lancer le 1v1
    if v1lancer == True:
        pressed = pygame.key.get_pressed()


        Bonus()
        # gerer le tir du joueur gauche (1)
        if chargeur1 > 0:
            if pressed[pygame.K_SPACE] and current_time - last_balle_time1 >= delay_balle:
                cooBalle1.append((25, y1 + joueur1.get_height()/2))
                last_balle_time1 = current_time
                chargeur1 -= 1
                canal_son_shoot.play(son_shoot)
        #...


        # gerer le tir du joueur droit (2)
        if chargeur2 > 0:
            if pressed[pygame.K_RETURN] and current_time - last_balle_time2 >= delay_balle:
                cooBalle2.append((1872, y2 + joueur2.get_height()/2))
                last_balle_time2 = current_time
                chargeur2 -= 1
                canal_son_shoot.play(son_shoot)
        #...

        # gerer les touches pressé par le joueur gauche (1)
        if y1 > 0:
            if pressed[pygame.K_z]:
                y1 -= 21
        if y1 < 1080 - joueur1.get_height():
            if pressed[pygame.K_s]:
                y1 += 21
        #...

        # gerer les touches pressé par le joueur droit (2)
        if y2 > 0:
            if pressed[pygame.K_UP]:
                y2 -= 21
        if y2 < 1080 - joueur2.get_height():
            if pressed[pygame.K_DOWN]:
                y2 += 21
        #...
        # afficher les deux joueur
        screen.blit(joueur1, (15, y1))
        screen.blit(joueur2, (1882, y2))
        #... 


    # retirer les balles qui sont en dehors de l'écran
        balles_a_supprimer1 = []
        balles_a_supprimer2 = []

        for update_balle1 in range(len(cooBalle1)):
            if cooBalle1[update_balle1][0] >= 1920:
                balles_a_supprimer1.append(update_balle1)

        for update_balle2 in range(len(cooBalle2)):
            if cooBalle2[update_balle2][0] <= 0:
                balles_a_supprimer2.append(update_balle2)

        for balle_index in balles_a_supprimer1:
            del cooBalle1[balle_index]

        for balle_index in balles_a_supprimer2:
            del cooBalle2[balle_index]
        # ...
            
        
        # afficher les balles du joueur gauche (1)
        for cooballe1 in range(len(cooBalle1)):
            if cooBalle1[cooballe1][0] >= 1870 and cooBalle1[cooballe1][0] <= 1894 and cooBalle1[cooballe1][1] >= y2 - 12 and cooBalle1[cooballe1][1] <= y2+joueur1.get_height() + 12:
                # si le joueur2 2 est touché par les balles 1
                point_joueur_1 += 1
                del cooBalle1[cooballe1]
                break
                #...
            
            # si le joueur gauche touche un bonus
            
            #...

            cooBalle1[cooballe1] = (cooBalle1[cooballe1][0] + 16, cooBalle1[cooballe1][1])
            pygame.draw.circle(screen, (0, 0, 255), (cooBalle1[cooballe1]), 12)
        #...


        # afficher les balles du joueur droit (2)
        for cooballe2 in range(len(cooBalle2)):
            if cooBalle2[cooballe2][0] <= 50 and cooBalle2[cooballe2][0] >= 38 and cooBalle2[cooballe2][1] >= y1 - 12 and cooBalle2[cooballe2][1] <= y1+joueur2.get_height() + 12:
                # si le joueur 2 est touché par les balles 1
                point_joueur_2 += 1
                del cooBalle2[cooballe2]
                break
                #...
            cooBalle2[cooballe2] = (cooBalle2[cooballe2][0] - 16, cooBalle2[cooballe2][1])
            pygame.draw.circle(screen, (255, 0, 0), (cooBalle2[cooballe2]), 12)
        #...



        # remettre les chargeurs a 10
        if chargeur1 == 0 and chargeur2 == 0:
            chargeur1 = 10
            chargeur2 = 10
        #...


        # afficher les flashs si les joueurs sont touché
        for cooballe1 in range(len(cooBalle1)):
            if cooBalle1[cooballe1][0] >= 1870 and cooBalle1[cooballe1][0] <= 1894 and cooBalle1[cooballe1][1] >= y2 - 12 and cooBalle1[cooballe1][1] <= y2+joueur1.get_height() + 12:
                canal_son_touch.play(son_touch)

        for cooballe2 in range(len(cooBalle2)):
            if cooBalle2[cooballe2][0] <= 50 and cooBalle2[cooballe2][0] >= 38 and cooBalle2[cooballe2][1] >= y1 - 12 and cooBalle2[cooballe2][1] <= y1+joueur2.get_height() + 12:
                canal_son_touch.play(son_touch)
        #...


        # afficher la taille des chargeurs
        font = pygame.font.SysFont(None, 30)
        text_chargeur1 = font.render("Chargeur 1: " + str(chargeur1), True, (255, 255, 255))
        text_chargeur2 = font.render("Chargeur 2: " + str(chargeur2), True, (255, 255, 255))
        font = pygame.font.SysFont(None, 100)
        text_point_joueur1 = font.render(str(point_joueur_1)    + "  |  " + str(point_joueur_2), True, (255, 0, 0))

        screen.blit(text_chargeur1, (50, 20))
        screen.blit(text_chargeur2, (1730, 20))
        screen.blit(text_point_joueur1, ((1920-text_point_joueur1.get_width())/2, 0))
        #...
    #...
#...


# jouer la musique
son_musique.play(-1)
#...

# fonction gerant les differante fonctions a appelé lors du 
def Game():

    # appeler la fonction menu au debut de la partie
    if choixOnglet == 'MenuMenu':
        Menu()
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
last_click_time = 0
#...

clock = pygame.time.Clock()

# boucle du jeu
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    # arriere plan en noir
    screen.fill((0, 0, 0))
    #...




    # appeler la fonction Game
    Game()
    # ...
        





    # mettre à jour l'écran
    pygame.display.flip()
    #...

    clock.tick(48)
# ...

pygame.quit()

import pygame
pygame.init()

# creer la fenetre
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("La Légendes d'Eldoria")
#...



# creer le Menu
police = pygame.font.SysFont('Comic Sans MS', 60, True, False)
titre = police.render("La Légende d'Eldoria", True, (255, 255, 0))

mape = pygame.image.load('Sprite/Map/map.png')
nMap = pygame.transform.scale(mape, (mape.get_width()*2, mape.get_height()*2))

texteStart = police.render('Explorer', True, (255, 0, 0))
bouton = pygame.image.load("Sprite/Bouton/Bouton.png")
rectBoutonStart = pygame.Rect(740, 440, 390, 198)

def MenuDepart():
    global Menu
    screen.fill((0, 0, 0))

    screen.blit(nMap, (-500, -500))

    screen.blit(titre, (620, 50))

    screen.blit(bouton, (700, 300))
    screen.blit(texteStart, (820, 490))
    
    if rectBoutonStart.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
        Menu = 0

    pygame.display.flip()
#...



# afficher les pages pour expliquer l'histoire
P1 = pygame.image.load("Sprite/TexteDebut/P1.png")
P2 = pygame.image.load("Sprite/TexteDebut/P2.png")
fleche = pygame.image.load("Sprite//TexteDebut/Fleche.png")
flecheRect = fleche.get_rect().move(1100, 930)
bouton2 = pygame.image.load("Sprite/Bouton/Bouton2.png")
rectBouton2 = pygame.Rect(680, 858, 405, 158)

def TexteDebut():
    global Textehistoire, page
    if page == 1:
        screen.fill((0, 0, 0))
        screen.blit(P1, (660, 0))
        screen.blit(fleche, (1100, 930))
        if flecheRect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            page = 2

    if page == 2:
        screen.fill((0, 0, 0))
        screen.blit(P2, (660, 0))
        screen.blit(bouton2, (650, 700))

        if rectBouton2.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            screen.fill((255, 255, 255))
            page = 3

    pygame.display.flip()


#...


# creer la gameloop
Menu = 1
page = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pos = pygame.mouse.get_pos()

    if Menu == 1:
        MenuDepart()
    if Menu == 0 and page == 1 or page == 2:
        TexteDebut()

pygame.quit()
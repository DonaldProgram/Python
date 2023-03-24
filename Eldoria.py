import pygame
pygame.init()

# creer la fenetre
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("La Légendes d'Eldoria")
#...




animation_speed = 120 # miliseconde
clock = pygame.time.Clock()



# animation moulin
moulin_sprite_sheet = pygame.image.load("Sprite/EffetVisuel/Moulin.png")

MoulinBig = pygame.transform.scale(moulin_sprite_sheet, (moulin_sprite_sheet.get_width()*2, moulin_sprite_sheet.get_height()*2))

Moulin_co1 = pygame.Rect(0, 0,  128, 128)
Moulin1 = MoulinBig.subsurface(Moulin_co1)

Moulin_co2 = pygame.Rect(128, 0, 128, 128)
Moulin2 = MoulinBig.subsurface(Moulin_co2)

Moulin_co3 = pygame.Rect(256, 0, 128, 128)
Moulin3 = MoulinBig.subsurface(Moulin_co3)

Moulin_co4 = pygame.Rect(384, 0, 128, 128)
Moulin4 = MoulinBig.subsurface(Moulin_co4)

MoulinMove = [Moulin1, Moulin2, Moulin3, Moulin4]

Moulin_choice = -1

# liste des position pour le moulin
position_moulins = [(-46, 620)]

def Moulin():
    global Moulin_choice
    for pos_moulin in position_moulins:
        screen.blit(MoulinMove[Moulin_choice], pos_moulin)
    
    Moulin_choice += 1

    if Moulin_choice == 3:
        Moulin_choice = -1
#...



# animer la fumer
fumee_sprite_sheet = pygame.image.load("Sprite/EffetVisuel/fumée.png")

fumee_co1 = pygame.Rect(0, 0, 32, 32)
fumee1 = fumee_sprite_sheet.subsurface(fumee_co1)

fumee_co2 = pygame.Rect(32, 0, 32, 32)
fumee2 = fumee_sprite_sheet.subsurface(fumee_co2)

fumee_co3 = pygame.Rect(64, 0, 32, 32)
fumee3 = fumee_sprite_sheet.subsurface(fumee_co3)

fumee_co4 = pygame.Rect(96, 0, 32, 32)
fumee4 = fumee_sprite_sheet.subsurface(fumee_co4)

fumee_co5 = pygame.Rect(128, 0, 32, 32)
fumee5 = fumee_sprite_sheet.subsurface(fumee_co5)

fumee_co6 = pygame.Rect(160, 0, 32, 32)
fumee6 = fumee_sprite_sheet.subsurface(fumee_co6)

fumee_move = [fumee1, fumee2, fumee3, fumee4, fumee5, fumee6]

fumee_choice = -1
coordonne_fumee_y = 475

time_wait_fumee = 0

def fumee():    
    global fumee_choice, coordonne_fumee_y, time_wait_fumee

    time_wait_fumee += clock.tick()

    if time_wait_fumee > 400:
        fumee_choice += 1
        screen.blit(fumee_move[fumee_choice], (500, coordonne_fumee_y))

        if fumee_choice == 5:            
            fumee_choice = -1
            coordonne_fumee_y = 475
        
        time_wait_fumee = 0

    coordonne_fumee_y -= 2

#...





# animation feu de camps
feuDeCamps_sprite_sheet = pygame.image.load("Sprite/DecorationSol/feuDeCamps.png")

feuDeCamps_co1 = pygame.Rect(0, 0,  32, 32)
feuDeCamps1 = feuDeCamps_sprite_sheet.subsurface(feuDeCamps_co1)

feuDeCamps_co2 = pygame.Rect(32, 0, 32, 32)
feuDeCamps2 = feuDeCamps_sprite_sheet.subsurface(feuDeCamps_co2)

feuDeCamps_co3 = pygame.Rect(64, 0, 32, 32)
feuDeCamps3 = feuDeCamps_sprite_sheet.subsurface(feuDeCamps_co3)

feuDeCamps_co4 = pygame.Rect(96, 0, 32, 32)
feuDeCamps4 = feuDeCamps_sprite_sheet.subsurface(feuDeCamps_co4)

feuDeCamps_move = [feuDeCamps1, feuDeCamps2, feuDeCamps3, feuDeCamps4]

feuDeCamps_choice = -1

def FeuCamps():
    global feuDeCamps_choice
    feuDeCamps_choice += 1
    screen.blit(feuDeCamps_move[feuDeCamps_choice], (500, 500))

    if feuDeCamps_choice == 3:
        feuDeCamps_choice = -1
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

    Moulin()
    FeuCamps()
    fumee()

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

    pygame.time.wait(animation_speed)


pygame.quit()

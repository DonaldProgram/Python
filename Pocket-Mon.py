# creer un jeu du style pokemon
import pygame
pygame.init()

# creer la fenetre
screen = pygame.display.set_mode((1915, 1040))
pygame.display.set_caption("Pocket-Mon")
#...

# variable pour gerer les fenetres a afficher
fenetre = "menu"
#...

# icon pokemon 
MenuPokemonTxt = pygame.image.load("Autre/MenuPokemonTxt.png")
Motismadex = pygame.image.load("Autre/Motismadex.png")
pokeballSimple = pygame.image.load("Autre/pokeballSimple.png")
pokestop = pygame.image.load("Autre/pokestop.png")
superball = pygame.image.load("Autre/superball.png")
oeuf = pygame.image.load("Autre/oeuf.png")

# Charger les images des pokemons
TortueMan = pygame.image.load("Pokemon/TortueMan.png")
GrosTasDeMorve = pygame.image.load("Pokemon/GrosTasDeMorve.png")
Pikachu = pygame.image.load("Pokemon/Pikachu.png")
#...
#...

# definir l'ecran du menu
def Menu():
    global fenetre
    while fenetre == "menu":
        # recuperer les touches presser
        pressed = pygame.key.get_pressed()
        #...

        # recuperer la position de la souris
        pos = pygame.mouse.get_pos()
        #...
        
        # pouvoir fermer la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fenetre = "Autre"
        #...
        # couleur de l'écran a blanc    
        screen.fill((255, 255, 255))
        #...   

        # afficher les icons sur l'ecran 
        screen.blit(MenuPokemonTxt, (300, 0))
        screen.blit(pokeballSimple, (30, 600))
        screen.blit(pokestop, (100, 900))
        screen.blit(superball, (600, 800))
        # afficher les pokemons sur l'ecran
        screen.blit(TortueMan, (600, 600))
        screen.blit(GrosTasDeMorve, (400, 800))
        screen.blit(Pikachu, (400, 50)) 
        #...
        #...

        # mise a jour de l'ecran
        pygame.display.flip()
        #...



# boucle principale
running = True
while running:
    # afficher la fenetre du menu
    Menu()
    #...

    # fermer la fenetre
    running = False
    pygame.quit()
    #...

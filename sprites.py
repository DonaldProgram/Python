import pygame
pygame.init()



class Bloc():
    Bedrock = pygame.image.load("Minecraft/Textures/Bloc/Bedrock.png")
    Pierres_cuites = pygame.image.load("Minecraft/Textures/Bloc/Pierres cuites.png")
    Bloc_Obsidienne = pygame.image.load("Minecraft/Textures/Bloc/Bloc d'obsidienne.png")
    Bloc_Or = pygame.image.load("Minecraft/Textures/Bloc/Bloc d'or.png")
    Bloc_Os = pygame.image.load("Minecraft/Textures/Bloc/Bloc d'os.png")
    Bloc_Charbon = pygame.image.load("Minecraft/Textures/Bloc/Bloc de charbon.png")
    Bloc_Cuivre1 = pygame.image.load("Minecraft/Textures/Bloc/Bloc de cuivre 1.png")
    Bloc_Cuivre2 = pygame.image.load("Minecraft/Textures/Bloc/Bloc de cuivre 2.png")
    Bloc_Cuivre3 = pygame.image.load("Minecraft/Textures/Bloc/Bloc de cuivre 3.png")
    Bloc_Diamant = pygame.image.load("Minecraft/Textures/Bloc/Bloc de diamants.png")
    Bloc_Fer = pygame.image.load("Minecraft/Textures/Bloc/Bloc de fer.png")
    Bloc_Lapis = pygame.image.load("Minecraft/Textures/Bloc/Bloc de lapis lazuli.png")
    Bloc_Verre1 = pygame.image.load("Minecraft/Textures/Bloc/Bloc de verre 1.png")


class Player():
    Joueur_ = pygame.image.load("Minecraft/Villageois/Joueur/Adam_16x16.png")
    Joueur_1 = Joueur_.subsurface(pygame.Rect(0, 0, 48, 96))


class Texte():
    Titre_Minecraft = pygame.image.load("Minecraft/Inventaire/Texte Minecraft.png")
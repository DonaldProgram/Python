# Importer le module pygame
import pygame
pygame.init()

# Classe permettant de créer tous les textes que l'on veut
class Texte:
    def __init__(self, police, taille, gras, lisser, **kwargs):
    # Utilisation:
    # police: "Nom de la police d'écriture"
    # taille: Nombre >= 0
    # gras: True/False
    # lisser: True/False
    # kwargs: "Mots à mesurer"

        if not isinstance(police, str):
            print("Le paramètre 'police' doit être une chaine de caractère !")
            exit()
        if not isinstance(taille, int) or taille <= 0:
            print("Le paramètre 'taille' doit être un entier positif !")
            exit()
        if not isinstance(gras, bool):
            print("Le paramètre 'gras' doit être égal à 'True/False'")
            exit()
        if not isinstance(lisser, bool):
            print("Le paramètre 'lisser' doit être égal à 'True/False'")
            exit()

        font = pygame.font.SysFont(police, taille, gras)
        nb_texte = 0
        for cle, texte in kwargs.items():
            nb_texte += 1
            surface_texte = font.render(texte, lisser, (255, 255, 255))
            print(f"{nb_texte}. {cle} : Longueur('{surface_texte.get_width()}px'), Hauteur('{surface_texte.get_height()}px')")
        print()

# Caractère à mesurer
character = Texte('Arial', 15, False, True, t1='Hi', t2='Hello man')
character = Texte('Arial Black', 100, False, True, t1='Hello', t2='HI')

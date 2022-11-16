import random
class Couleur:
    Bleu = '\033[94m' 
    Rouge = '\033[91m' 
    Normal = '\033[0m'
    Violet = '\033[95m'
    Blanc = '\033[97m' 

    Noire = '\033[30m'
    Vert = '\033[32m'
    Orange = '\033[33m'
    Cyan = '\033[36m'
    Gris = '\033[90m'
    RougeClair = '\033[91m'
    VertClair = '\033[92m'
    Jaune = '\033[93m'
    Rose = '\033[95m'
    CyanClair = '\033[96m'

class BlackJack:
    """
        Represente un jeu BlackJack.
    """

    def __init__(self):
        self.cagnotte = 10
        self.choixCagnotte = None
        self.listeCartes = [2, 2 , 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
        self.tiragesJoueur = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.tiragesCroupier = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.tour = 0
        self.gagnant = None
        self.actionDuJoueur = None

    def run(self):
        ...
        #
        # Affiche la cagnotte
        # 
        self.afficheCagnotte()
    
        #
        # Demande la mise au joueur
        #
        self.demandeLaMiseDuJoueur()

        #
        # Boucle du jeu 
        # 
        while True:
            self.tour += 1

            #  
            # Demande au joueur de tirer ou rester
            #  
            self.actionDuJoueur = None
            self.demandeAuJoueurDeTirerOuRester()

            #  
            # Si le joueur tire 
            # 
            if self.actionDuJoueur == 't':
                self.tirerCarte('j')
                if self.quiAGagne() != 'j':
                    self.tirerCarte('c')

            #  
            # Si le joueur reste
            #
            elif self.actionDuJoueur == 'r':
                while sum(self.tiragesCroupier) < 17:
                    self.tirerCarte('c')
                    self.afficheTableauDesCartes()
                    self.tour += 1
                
                self.afficheLesGainsDuGagnant()
                
                return

            else:
                break

            #  
            # Affiche toutes les cartes ainsi que les totaux du joueur et du croupier
            #  
            self.afficheTableauDesCartes()

            #
            # Break s'il y a un gagnant
            #
            if self.quiAGagne() != "":
                break

        #  
        # Affiche les gains du gagnant
        #  
        self.afficheLesGainsDuGagnant()

    def afficheCagnotte(self):
        print("Votre cagnotte est de", self.cagnotte, "€")

    def demandeLaMiseDuJoueur(self):
        while True:
            try:
                self.choixCagnotte = int(input("Choix mises : "))
                while self.choixCagnotte > 10 or self.choixCagnotte < 1:
                    if self.choixCagnotte > self.cagnotte:
                        print('Mises trop élevé')
                        self.choixCagnotte = int(input("Choix mises : "))
                    elif self.choixCagnotte < 1:
                        print("Mise trop petite")
                        self.choixCagnotte = int(input("Choix mises : "))
                break
            except ValueError:
                print("Ce n'est pas un nombre")

    def demandeAuJoueurDeTirerOuRester(self):
        while self.actionDuJoueur == None:
            action = input("Tirer ou rester (t ou r) -> ")
            if action == 't' or action == 'r':
                self.actionDuJoueur = action
                break

    def afficheTableauDesCartes(self):
        print(Couleur.Bleu + "Joueur :  ", self.tiragesJoueur, "Total :", sum(self.tiragesJoueur), Couleur.Normal)
        print(Couleur.Rouge + "Croupier :", self.tiragesCroupier, "Total :", sum(self.tiragesCroupier), Couleur.Normal)

    def quiAGagne(self):
        if sum(self.tiragesJoueur) > 21:
            return "c"
        elif sum(self.tiragesCroupier) > 21:
            return "j"
        elif sum(self.tiragesJoueur) == 21:
            return "j"
        elif sum(self.tiragesCroupier) == 21:
            return "c"
        elif sum(self.tiragesJoueur) < sum(self.tiragesCroupier) <= 21:
            return "c"
        else:
            return ""

    def afficheLesGainsDuGagnant(self):
        if self.quiAGagne() == "j":
            self.cagnotte -= self.choixCagnotte
            self.choixCagnotte *= 2
            self.cagnotte += self.choixCagnotte 
            print("Le joueur a gagné", self.cagnotte - self.choixCagnotte, "€")
            print("La cagnotte est de",self.cagnotte, "€")
        elif self.quiAGagne() == "c":
            print("Le joueur a perdu", self.choixCagnotte, "€")
            print("La cagnotte est de",self.cagnotte, "€")
        else:
            print("Pas de gagnant")
            print("La cagnotte est de",self.cagnotte, "€")

    def tirerCarte(self, qui):
        if qui == 'j':
            self.tiragesJoueur[self.tour-1] = random.choice(self.listeCartes)
            self.listeCartes.remove(self.tiragesJoueur[self.tour-1])
        elif qui == 'c':
            self.tiragesCroupier[self.tour-1] = random.choice(self.listeCartes)
            self.listeCartes.remove(self.tiragesCroupier[self.tour-1])   
        else:
            exit()

BlackJack().run()

import time,random
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
    Gris = '\033[90m'               # Utiliser
    RougeClair = '\033[91m'
    VertClair = '\033[92m'
    Jaune = '\033[93m'              # Utiliser
    Rose = '\033[95m'
    CyanClair = '\033[96m'


listeCalcule = list(range(-50 , 50+1))
cagnotte = 0
suite = 0
choixOnglet = "principal"
# Variable competences
Calculator = 0
Mineur = 0
Constructeur = 0
Programmeur = 0


def Espace(pause,Inferieur):
    espace2 = ""
    nbEspace2 = 0
    time.sleep(pause)
    while nbEspace2 < Inferieur:
        print("")
        espace2 += " "
        nbEspace2 += 1

def AfficheCagnotte():
    print("Vous avez " + str(cagnotte) + "€")


def PremiereOrdinateur():
    print("")
    print(Couleur.Gris +"   __|\____      ___")
    print(              "  |  144p  |    |   |")
    print(              " /|________|\   |   |")
    print(              "/___|    |___\  |___|")
    print(              "   _______ ")
    print(              "  |_______| 0 ")


def PuissantOrdinateur():
    print(Couleur.Bleu + " _________")
    print(               "|", Couleur.Violet + "1080p8K", Couleur.Bleu +"|")
    print(               "|_________|" + Couleur.Normal)

    print(Couleur.Rouge + "              _")
    print(Couleur.Vert +  "   ____     ", Couleur.Rouge + "| |")
    print(Couleur.Vert +  "  |____| 0  ", Couleur.Rouge + "|_|")


def PCmoyens():
    print(Couleur.Bleu + "_______")
    print("|_____|")
    print("  ___")
    print(" |___| 0")


def PCportable():
    print(Couleur.Jaune + " ____")
    print("|____|")
    print(" |__| 0")
    print(" ")

# Creation fonctions des menus
def MenuPrincipal():
    global suite
    if choixOnglet == "principale":
        suite = 0
        Espace(0, 100)
        print("Menu :",Couleur.Jaune +" PRINCIPAL" + Couleur.Normal)
        print("Ordinateur (o)")
        print("Calculs (c)")
        print("Competences (l)")
        while suite == 0:
            try:
                reponse = str(input("Aller dans l'onglet : "))
                if reponse == str(reponse):
                    if str(reponse) == "o":
                        suite = 1
                        choixOnglet = "ordinateur"
                    
                    elif str(reponse) == "c":
                        suite = 1
                        choixOnglet = "calcul"

                    elif str(reponse) == "l":
                        suite = 1
                        choixOnglet = "competence"                    
            except SyntaxError:
                ...


def Calcule():
    global choixOnglet
    if choixOnglet == "calcul":
        suite = 0
        Espace(0, 100)
        gain = 0
        while gain != 300:
            global cagnotte
            nbCalculeOK = 0
            nombre1 = random.choice(listeCalcule)
            nombre2 = random.choice(listeCalcule)
            print(nombre1, "+", nombre2)
            reponseOrdinateur = nombre1 + nombre2
            while nbCalculeOK == 0:
                try:
                    reponse = int(input("Reponse = "))
                    if reponse == int(reponse):
                        nbCalculeOK = 1
                        gain += 50
                except ValueError:
                    ...
            if int(reponse) == reponseOrdinateur:
                print(Couleur.Vert + "Juste, vous gagner 50€." + Couleur.Normal)
                cagnotte += 50
                Espace(2, 100)
                AfficheCagnotte()
                Espace(2, 100)
            elif int(reponse) != reponseOrdinateur:
                print(Couleur.Rouge + "Faux, vous ne gagnez rien." + Couleur.Normal)
                Espace(2, 100)
                AfficheCagnotte()
                Espace(2, 100)
    choixOnglet = "principale"


def Competence(): 
    if choixOnglet == "competence":   
        suite = 0 
        Espace(0, 100)
        print("Menu",Couleur.Jaune + "COMPETENCE" + Couleur.Normal)
        print("Calculer Lvl",Calculator)
        print("Mineur Lvl", Mineur)
        print("Constructeur Lvl", Constructeur)
        print("Programmeur Lvl", Programmeur)
        print("Principal (p)")
        try:
            while suite == 0:
                reponse = str(input("Allez dans l'onglet : "))
                if reponse == str(reponse):
                    if str(reponse) == "p":
                        choixOnglet = "principale"
                        suite = 1
        except SyntaxError:
            ...


def Ordinateur():
    if choixOnglet == "ordinateur":
        suite = 0
        Espace(0, 100)
        print("Menu", Couleur.Jaune + "Ordinateur")
        print("BTC (b)")
        print("Acheter objet (a)")
        print("Menu principal (p)")
        print("Chercher travail (t)")
        print("Creer Entreprise (e)")
        try:
            while suite == 0:
                reponse = str(input("Aller dans l'onglet : "))
                if reponse == str(reponse):
                    if str(reponse) == "b":
                        choixOnglet = "btc"
                        suite = 1

                    elif str(reponse) == "a":
                        choixOnglet = "shopObjet"
                        suite = 1

                    elif str(reponse) == "p":
                        choixOnglet = "principale"
                        suite = 1                    

                    elif str(reponse) == "t":
                        onglet = "chercherTravail"
                        suite = 1
                    elif str(reponse) == "e":
                        choixOnglet = "entreprise"
                        suite = 1
        except SyntaxError:
            ...



def BTC():
    if choixOnglet == "btc":
        suite = 0
        Espace(0, 100)
        print("Menu", Couleur.Jaune + "BTC")
        print("Miner BTC (m)")
        print("Acheter BTC (a)")
        print("Principale (p)")
        try:
            while suite == 0:
                reponse = str(input("Aller dans l'onglet : "))
                if reponse == (str(reponse)):
                    if str(reponse) == "m":
                        choixOnglet = "miner BTC"
                        suite = 1
                    elif str(reponse) == "a":
                        choixOnglet = "acheter BTC"
                        suite = 1
                    elif str(reponse) == "p":
                        choixOnglet = "principale"
                        suite = 1

        except SyntaxError:
            ...


def minerBTC():
    if choixOnglet == "miner BTC": 
        suite = 0 
        Espace(0, 100)
        print("Minage en cours...")
        Espace(4, 100)
        print("Vous avez gagné 16€")
        cagnotte += 16
        Espace(2, 100)
        AfficheCagnotte()
        time.sleep(2)
        choixOnglet = "principale"


def AcheterBTC():
    if choixOnglet == "acheter BTC": 
        suite = 0
        Espace(0, 100)
        try:
            while suite == 0:
                reponse = int("Pour combien d'euros voulez vous achetez : ")
                if reponse == int(reponse):
                    if int(reponse) <= cagnotte:
                        cagnotte -= int(reponse)
                        Espace(3, 100)
                        print("Vous avez acheter", str(reponse) + "€ de Bitcoin.")
                        AfficheCagnotte()
                        suite = 1
                        time.sleep(2)
                        choixOnglet = "principale"
        except ValueError:
            ...


def Shop():
    if choixOnglet == "shopObjet":
        suite = 0
        Espace(0, 100) 
        print("Menu", Couleur.Jaune + "SHOP")
        print("Ordinateur (o)")
        print("Maison (m)")
        print("Voiture (v)")
        print("Bateau (b)")
        print("Principal (p)")
        try:
            while suite == 0:
                reponse = str(input("Aller dans l'onglet : "))
                if reponse == str(reponse):
                    if str(reponse) == "o":
                        choixOnglet = "ShopOrdinateur"
                        suite = 1 
                    elif str(reponse) == "m":
                        choixOnglet = "maison"
                        suite = 1
                    elif str(reponse) == "v":
                        choixOnglet = "voiture"
                        suite = 1
                    elif str(reponse) == "b":
                        choixOnglet = "bateau"
                        suite = 1
                    elif str(reponse) == "p":
                        choixOnglet = "principale"
                        suite = 1
        except SyntaxError:
            ...


def Travail():
    suite = 0
    if choixOnglet == "chercherTravail":
        Espace(0, 100)
        print("Menu", Couleur.Jaune + "CHERCHER TRAVAIL")
        print("Travaux rapides (r)")
        print("Travaux long (l)")
        try:
            while suite == 0:
                reponse = str(input("Allez dans l'onglet : "))
                if reponse == str(reponse):
                    if str(reponse) == "r":
                        choixOnglet = "travaux rapides"
                        suite = 1
                    elif str(reponse) == "l":
                        choixOnglet = "travaux long"
                        suite = 1
        except SyntaxError:
            ...


def AcheterOrdinateur():
    global cagnotte, suite
    print("Menu", Couleur.Jaune + "Acheter Ordinateur :" + Couleur.Normal)
    print("")
    print("Ordinateur Surpuissant:")
    print("Prix :", couleur.Jaune + "11000")
    PuissantOrdinateur()
    print(Couleur.Normal + "Acheter Ordinateur Surpuissant (s)")
    print("")
    print(Couleur.Normal + "Ordinateur Moyens :")
    print("Prix :", couleur.Jaune + "1500")    
    PCmoyens()
    print(Couleur. Normal + "Acheter Ordinateur Moyens (m)")
    print("")
    print("Prix :", couleur.Jaune + "6000")
    PCportable()
    print(Couleur.Normal + "Acheter Ordinateur Portable (l)" + Couleur.Normal)
    print("")
    print("Principal (p)")
    print("")
    try:
        while suite == 0:
            reponse = str(input("Aller dans l'onglet : "))
            if reponse == str(reponse):
                if str(reponse) == "s":
                    if cagnotte >= 11000:
                        cagnotte -= 11000
                        Espace(0, 100)
                        print("Vous avez recu (Ordinateur Surpuissant)")
                        Espace(2, 100)
                        AfficheCagnotte()
                        suite = 1
                        choixOnglet = "principale"
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent pour acheter cet ordinateur.")
                        Espace(2, 100)
                        suite = 1
                        choixOnglet = "principale"  

                elif str(reponse) == "m":
                    if cagnotte >= 1500:
                        cagnotte -= 1500
                        Espace(0, 100)
                        print("Vous avez recu (Ordinateur Moyens)")
                        Espace(2, 100)
                        AfficheCagnotte()
                        suite = 1
                        choixOnglet = "principale"
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent pour acheter cet ordinateur.")
                        Espace(2, 100)
                        suite = 1
                        choixOnglet = "principale"  

                elif str(reponse) == "l":
                    if cagnotte >= 6000:
                        cagnotte -= 6000
                        Espace(0, 100)
                        print("Vous avez recu (Ordinateur Portable)")
                        Espace(2, 100)
                        AfficheCagnotte()   
                        suite = 1
                        choixOnglet = "principale"                   
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent pour acheter cet ordinateur." + Couleur.Normal)
                        Espace(2, 100)
                        suite = 1
                        choixOnglet = "principale"
                
                elif str(reponse) == "p":
                    suite = 1
                    choixOnglet = "principale"
    except SyntaxError:
        ...


def CabaneBois():
    print(Couleur.Vert + " __________")
    print(               " |   __   |")
    print(               " |  |  |  |")
    print(               " |__|__|__|" + Couleur.Normal)


def PetiteMaison():
    print(Couleur.Gris + "  ________")
    print(               " /        \ " )
    print(               "/__________\ ")
    print(               " |   __   |")
    print(               " |  |  |  |")
    print(               " |__|__|__|" + Couleur.Normal)


def GrandeMaison():
    print("                      O")
    print("    _________________   O")
    print("   /                 \ | |")
    print("  /                   \| |")
    print(" /                     \_|        " )
    print("/_______________________\ ")
    print(" |   _____     _____   |")
    print(" |  |__|__|   |__|__|  |")
    print(" |  |__|__|   |__|__|  |")
    print(" |         __          |")
    print(" |        |  |         |")
    print(" |________|__|_________|")


def MaisonDeLuxe():
    print("                      O")
    print("    _________________   O")
    print("   /                 \ | |")
    print("  /                   \| |")
    print(" /                     \_|_________" )
    print("/_______________________\ /        \ ")
    print(" |   _____     _____   | /          \  ")
    print(" |  |__|__|   |__|__|  |/____________\ ")
    print(" |  |__|__|   |__|__|  |              |")
    print(" |         __          |      __      |")
    print(" |        |  |         |     |  |     |")
    print(" |________|__|_________|_____|__|_____|")

def AcheterMaison():
    global cagnotte
    suite = 0
    print("Menu", Couleur.Jaune + "ACHETER MAISON")
    print("")
    print(Couleur.Normal + "Prix :", Couleur.Jaune + "150€")
    CabaneBois()
    print("Acheter cabane de bois (b)")
    print("")
    print(Couleur.Normal + "Prix :", Couleur.Jaune + "15.000€")
    PetiteMaison()
    print("Acheter petite maison (m)")
    print("")
    print("Prix :", Couleur.Jaune + "95.000€" + Couleur.Normal)
    GrandeMaison()
    print("Acheter Grande maison (g)")
    print("")
    print("Prix :", Couleur.Jaune + "200.000€" + Couleur.Normal)
    MaisonDeLuxe()
    print("Acheter Maison de luxe (l)")
    print("")
    print("Principal (p)")
    try:
        while suite == 0:
            reponse = str(input("Aller dans l'onglet : "))
            if reponse == str(reponse):
                if str(reponse) == "b":
                    if cagnotte >= 150:
                        print("Vous avez recu (cabane de bois)")
                        cagnotte -= 150
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        suite = 1
                        choixOnglet = "principale"
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent pour acheter cette maison")
                        time.sleep(2)
                        suite = 1
                        choixOnglet = "principale"

                elif str(reponse) == "m":
                    if cagnotte >= 15000:
                        print("Vous avez recu (Petite maison)")
                        cagnotte -= 15000
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        suite = 1
                        choixOnglet = "principale"
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent pour acheter cette maison")
                        time.sleep(2)
                        suite = 1
                        choixOnglet = "principale"
                
                elif str(reponse) == "g":
                    if cagnotte >= 95000:
                        cagnotte -= 95000
                        print("Vous avez recu (Grande Maison)")
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        suite = 1
                        choixOnglet = "principale"
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent pour acheter cette maison")
                        time.sleep(2)
                        suite = 1
                        choixOnglet = "principale"
                
                elif str(reponse) == "l":
                    if cagnotte >= 200000:
                        cagnotte -= 200000
                        print("Vous avez recu (Maison de luxe)")
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        suite = 1
                        choixOnglet = "principale"
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent pour acheter cette maison")
                        time.sleep(2)
                        suite = 1
                        choixOnglet = "principale"
                elif str(reponse) == "p":
                    choixOnglet = "principale"
                    suite = 1

    except SyntaxError:
        ...


def VoitureNul():
    print(Couleur.Vert + "   _______")
    print(               "  / || || \__")
    print(               "   O---------O" + Couleur.Normal)


def VoiturePetite():
    print(Couleur.Vert + "    _____")
    print(               "   /  || \_")
    print(               "   O-------O" + Couleur.Normal)


def Fourgons():
    print("   __________")
    print("o o|_||_||_|_\ ")
    print("    O       O")


def Train():
    print(Couleur.Bleu + " ---    ---- --- -  ____________________")
    print(               "---    - -- -----  |____________________\ ")


def AcheterVoiture():
    global cagnotte
    suite = 0
    print("Menu",Couleur.Jaune + "Acheter Voiture" + Couleur.Normal)
    print("")
    print("Prix :", Couleur.Jaune + "7.000€" + Couleur.Normal)
    VoitureNul()
    print("Acheter Voiture Nul (n)")
    print("")
    print("Prix :", Couleur.Jaune + "15.000€" + Couleur.Normal)
    VoiturePetite()
    print("Acheter Petite Voiture (l)")
    print("")
    print("Prix :", Couleur.Jaune + "27.000€" + Couleur.Normal)
    Fourgons()
    print("Acheter Fourgons (f)")
    print("")
    print("Prix :", Couleur.Jaune + "160.000€" + Couleur.Normal)
    Train()
    print(Couleur.Normal + "Acheter Train (t)")
    print("")
    print(Couleur.Normal + "Principale (p)")
    try:
        while suite == 0:
            reponse = str(input("Acheter : "))
            if reponse == str(reponse):
                if str(reponse) == "n":
                    if cagnotte >= 7000:
                        choixOnglet = "voiture nul"
                        cagnotte -= 7000
                        Espace(0, 100)
                        print("Vous avez recu (voiture nul)")
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        choixOnglet = "principale"
                        suite = 1
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent")
                        Espace(2, 100)
                        choixOnglet = "principale"
                        suite = 1

                if str(reponse) == "l":
                    if cagnotte >= 15000:
                        choixOnglet = "voiture nul"
                        cagnotte -= 15000
                        Espace(0, 100)
                        print("Vous avez recu (Petite Voiture)")
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        choixOnglet = "principale"
                        suite = 1
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent")
                        Espace(2, 100)
                        choixOnglet = "principale"
                        suite = 1
                
                if str(reponse) == "f":
                    if cagnotte >= 27000:
                        choixOnglet = "voiture nul"
                        cagnotte -= 27000
                        Espace(0, 100)
                        print("Vous avez recu (Fourgons)")
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        choixOnglet = "principale"
                        suite = 1
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent")
                        Espace(2, 100)
                        choixOnglet = "principale"
                        suite = 1
                
                if str(reponse) == "t":
                    if cagnotte >= 160000:
                        choixOnglet = "voiture nul"
                        cagnotte -= 160000
                        Espace(0, 100)
                        print("Vous avez recu (Train)")
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        choixOnglet = "principale"
                        suite = 1
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent")
                        Espace(2, 100)
                        choixOnglet = "principale"    
                        suite = 1
    except SyntaxError:
        ...


def TravauxRapides():
    global cagnotte
    if choixOnglet == "travaux rapides":
        Espace(0, 100)
        print("Debut travaux rapides (10s)")
        Espace(10, 100)
        print("Vous avez gagné 150 euros")
        cagnotte += 150
        Espace(2, 100)
        AfficheCagnotte()


choixOnglet = "travaux rapides"
def TravauxLong():
    global cagnotte
    if choixOnglet == "travaux rapides":
        Espace(0, 100)
        print("Debut travaux rapides (20s)")
        Espace(20, 100)
        print("Vous avez gagné 400 euros")
        cagnotte += 400
        Espace(2, 100)
        AfficheCagnotte()


def PetitBatiment():
    print(Couleur.Gris + "_________")
    print(               "| || || |")
    print(               "| || || |")
    print(               "|_______|")


def BatimentMoyens():
    print("_______________")
    print("| || || || || |")
    print("| || || || || |")
    print("| || || || || |")
    print("| || || || || |")
    print("|_____________|")


def BatimentGrand():
    print("_____________________")
    print("| || || || || || || |")
    print("| || || || || || || |")
    print("| || || || || || || |")
    print("| || || || || || || |")
    print("|___________________|")


def BatimentLuxe():
    print(Couleur.Bleu +  "________________________")
    print(Couleur.Jaune + "|" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" +  Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-"+ Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Vert + "|")
    print(Couleur.Rouge + "|" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" +  Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Bleu + "-"+ Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Vert + "|")
    print(Couleur.Vert +  "|" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" +  Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Bleu + "-"+ Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Vert + "|")
    print(Couleur.Bleu +  "|" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" +  Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Bleu + "-"+ Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Vert + "|")                      
    print(Couleur.Jaune + "|" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" +  Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-"+ Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Vert + "|")                      
    print(Couleur.Rouge + "|" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" +  Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Bleu + "-"+ Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Vert + "|")                      
    print(Couleur.Vert +  "|" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" +  Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Bleu + "-"+ Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Vert + "|")                      
    print(Couleur.Bleu +  "|" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" +  Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Bleu + "-"+ Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Vert + "|")
    print(Couleur.Jaune + "|" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Bleu + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" +  Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-"+ Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Vert + "|")                      
    print(Couleur.Rouge + "|" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Jaune + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" +  Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-"+ Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert  + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "|")                      
    print(Couleur.Vert +  "|" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Rouge + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" +  Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-"+ Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "-" + Couleur.Jaune + "-" + Couleur.Rouge + "-" + Couleur.Vert + "-" + Couleur.Bleu + "|")                      
    print(Couleur.Bleu +  "|         ____         |")    
    print(Couleur.Jaune + "|        " + Couleur.Bleu +  "|    |"+ Couleur.Jaune + "        |")
    print(Couleur.Rouge  +"|________" +  Couleur.Bleu + "|____|" + Couleur.Rouge + "________|") 


def EntrepriseBatiment():
    global choixOnglet, cagnotte
    if choixOnglet == "entreprise" :
        suite = 0
        print("Menu", Couleur.Jaune + "Creer votre entreprise" + Couleur.Normal)
        print("Choix Batiment : ")
        print('')
        print("Prix", Couleur.Jaune + "30.000€" + Couleur.Normal)
        PetitBatiment()
        print(Couleur.Normal + "Acheter Petit Batiment (n)")
        print('')
        print(Couleur.Normal + "Prix", Couleur.Jaune + "70.000€" + Couleur.Normal)
        BatimentMoyens()
        print("Acheter Batiment Moyens (m)")
        print("")
        print(Couleur.Normal + "Prix", Couleur.Jaune + "115.000€" + Couleur.Normal)
        BatimentGrand()
        print("Acheter Batiment Grand (g) ")
        print('')
        print(Couleur.Normal + "Prix", Couleur.Jaune + "70.000€" + Couleur.Normal)
        BatimentLuxe()
        print(Couleur.Normal + "Acheter Batiment de luxe (l)")
        print('')
        print("Principale (p)")
        try:
            while suite == 0:
                reponse = str(input("Choix Batiment : "))
                if str(reponse) == "n":
                    if cagnotte >= 30000:
                        cagnotte -= 30000
                        print("Vous avez recu Petit Batiment")
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        suite = 1
                        choixOnglet = "nbEmployés"
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent.")
                        Espace(2, 100)
                        choixOnglet = "principale"
                        suite = 1
                    
                elif str(reponse) == "m":
                    if cagnotte >= 70000:
                        print("Vous avez recu Batiment moyens")
                        cagnotte -= 70000
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        suite = 1
                        choixOnglet = "nbEmployés"
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent.")
                        Espace(2, 100)
                        choixOnglet = "principale"
                        suite = 1
               
                elif str(reponse) == "g":
                    if cagnotte >= 115000:
                        print("Vous avez recu Batiment Grand")
                        cagnotte -= 115000
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        suite = 1
                        choixOnglet = "nbEmployés"
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent.")
                        Espace(2, 100)
                        choixOnglet = "principale"
                        suite = 1

                elif str(reponse) == "l":
                    if cagnotte >= 300000:
                        print("Vous avez recu Batiment de Luxe")
                        cagnotte -= 300000
                        Espace(2, 100)
                        AfficheCagnotte()
                        Espace(2, 100)
                        suite = 1
                        choixOnglet = "nbEmployés"
                    else:
                        print(Couleur.Rouge + "Vous n'avez pas assez d'argent.")
                        Espace(2, 100)
                        choixOnglet = "principale"
                        suite = 1
                    
                elif str(reponse) == "p":
                    Espace(0, 100)
                    choixOnglet = "principale"
                    suite = 1
        except SyntaxError:
            ...
# Pour animation du debut

Debut = 0
espace = ""
nbEspace = 0
a = 0
barre = "-"
nbBarre = 0
Suite = 0
EcranHauteur = 0
Lancement = 0

while Debut == 0:
    try:
        Lanceur = str(input("Lancer le jeu(j) = "))
        if Lanceur == "j":
            Debut = 1
    except SyntaxWarning:
        ...

while Suite == 0:
    while a < 25:
        print('')
        a +=1
    if nbEspace > 205:
        espace = ""
        nbEspace = 0
        Suite = 1
    if nbBarre > 205:
        barre =  "-"
        Suite = 1
        nbBarre = 0
    espace += " "
    barre += "-"
    nbBarre += 1
    nbEspace += 1
    
    if Suite == 0:
        while Lancement < 40:
            print("")
            Lancement += 1
        Lancement = 0

        time.sleep(0.1)
        print(Couleur.Jaune + "       ____")
        print(                "      |    |")
        print(                "      |____|"+ Couleur.Normal)
        print(Couleur.Gris+" _______ ___ _____   __          __ ___ _ ________ __ _ __________ ______ ____ _ _ ___ __ _ _ _ __ _ __ __   ___________      ________ __    ___ _ __ _ __ _ __ _____ _ ________________   __ _ ______ __ ___ _______   __ ______ __")
        print("_______ __________      _______    ____     _ _ _______ __ ____ _          ________ _ _ _ ______ _ ________ __ __ __ ___           ___ _  _ _ ____ ___ __ __ ______ __ ___ _________ ______ __ __ __ __     __ _ __    _ _ _ _______ " + Couleur.Normal)


        while Lancement < 7:
            print("")
            Lancement += 1
        Lancement = 0

        print(espace + Couleur.Vert + "   _______")
        print(espace +                "  / || || \__")
        print(espace +                "   O---------O" + Couleur.Normal)
        print(Couleur.Jaune + "----------------------"+barre) 

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0

print(Couleur.Normal + "DEBUT DU JEU ....")
time.sleep(3)

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0

print("Chargement en cours 20%")
time.sleep(1.5)

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0
print("Chargement en cours 40%")
time.sleep(1.5)

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0
print("Chargement en cours 60%")
time.sleep(1.5)

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0
print("Chargement en cours 80%")
time.sleep(1.5)

while Lancement < 100:
    print("")
    Lancement += 1
Lancement = 0

print("Chargement en cours 100%")
time.sleep(3)

while Lancement < 100:
    print("")
    Lancement += 1

# Debut du jeu 
espace2 = ""
nbEspace2 = 0
b = 0
tourPersonnage = 0
while tourPersonnage < 8:
    tourPersonnage += 1
    if b == 0:
        Espace(0.4, 100)
        print(" O/")
        print("/| <- Sa c'est vous")
        print("/ \ ")

        b = 1

    if b == 1:
        Espace(0.4, 100)
        print(" O__")
        print("/| <- Sa c'est vous")
        print("/ \ ")     
        b = 0

# Gagne cagnotte
Espace(0, 100)
print(" O")
print("/|\ Votre but est d'avoir une bonne vie")
print("/ \ ")

Espace(6, 100)
print(" O")
print("/|\ Votre premiere mission est de gagner de l'argent")
print("/ \ ")

Espace(6, 100)
print(" O")
print("/|\ Pour cela un quizz de question determinera votre capitale de depart")
print("/ \ ")

# Debut du quizz

Espace(6, 100)
print("C'est partit :)")

Espace(2, 100)
AfficheCagnotte()

Espace(3, 100)
reponse = input("1 + 1 = ")
if reponse == "2":
    cagnotte += 2
    print("Juste, Vous gagné 2€")
    Espace(3, 100)
    AfficheCagnotte()
    Espace(3, 100)
else:
    print("Faux, Vous ne gagnez rien")
    Espace(3, 100)
    AfficheCagnotte()
    Espace(3, 100)

# Jeux
nbQuestion = 0
choixOnglet = "calcul"
while cagnotte < 300:
    Calcule()
    nbQuestion += 1


# Achat premiere ordinateur

Espace(3, 100)
print("Maintenant que tu as un peu d'argent, allons acheter ton premier ordinateur.")
Espace(6, 100)
PremiereOrdinateur()
print("")
while cagnotte != 150:
    try:
        reponse = str(input(Couleur.Normal + "Appuie sur a pour l'acheter : "))
        if reponse == str(reponse):
            if str(reponse) == "a":
                cagnotte -= 150
                Espace(0, 100)
                print("Tu as recupere (ordinateur ancien)")
                Espace(3, 100)
                AfficheCagnotte()
    except SyntaxError:
        ...

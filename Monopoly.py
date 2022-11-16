# le jeu du monopoly
import random
import time

# Changer le texte de couleur
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


# Creation des cases
CaseDepartHAUT = Couleur.Normal +      '|  DEPART  |'
CaseDepartBAS =  Couleur.Normal +      '|   200$   |'


RueDeLaPaixHAUT = Couleur.Bleu +       '|  RUE DE  |'
RueDeLaPaixBAS = Couleur.Bleu +        '|  LA PAIX |'
PrixRuePaix = Couleur.Blanc   +        '|   $400   |' 


TaxeDeLuxeHAUT = Couleur.Blanc +       '|  TAXE DE |'
TaxeDeLuxeBAS = Couleur.Blanc +        '|   LUXE   |'
PrixTaxeDeLuxe = Couleur.Blanc   +     '|   $100   |' 


ChampsElyséeHAUT = Couleur.Bleu +      '|  CHAMPS  |'
ChampsEliséeBAS = Couleur.Bleu +       '|  ÉLYSÉES |'
PrixChampsElysée = Couleur.Blanc  +    '|   $350   |' 


CaseChanceHAUT = Couleur.Rose +        '|     ?    |'
CaseChanceBAS = Couleur.Bleu +        '|  CHANCE  |'


GareSaintLazareHAUT = Couleur.Noire + '|   SAINT  |'
GareSaintLazareBAS = Couleur.Noire +  '|  LAZARE  |'
PrixGareSaintLazare = Couleur.Blanc  +'|   $200   |' 


CapucinesHAUT = Couleur.VertClair +   '| BOULEVARD|'
CapucineBAS = Couleur.VertClair +     '| CAPUCINES|'
PrixCapucine = Couleur.Blanc   +      '|   $320   |' 


CaisseCommunautéHAUT = Couleur.Bleu +  '| CAISSE DE|'
CaisseCommunautéBAS = Couleur.Bleu +   '|COMMUNAUTÉ|'


FochHAUT = Couleur.VertClair +         '|   AVENUE |'
FochBAS = Couleur.VertClair +          '|   FOCH   |'
PrixFoch = Couleur.Blanc   +           '|   $300   |' 


BreteuilHAUT = Couleur.VertClair +     '| AVENUE DE|'
BreteuilBAS = Couleur.VertClair +      '| BRETEUIL |'
PrixBreteuil = Couleur.Blanc   +       '|   $300   |' 


AllezPrisonHAUT = Couleur.Noire +      '| ALLEZ EN |'
AllezPrisonBAS = Couleur.Noire +       '|  PRISON  |'


FayetteHAUT = Couleur.Jaune +          '|  RUE LA  |'
FayetteBAS = Couleur.Jaune +           '| FAYETTE  |'
PrixFayette = Couleur.Blanc   +        '|   $280   |' 


CompagniesEauxHAUT = Couleur.Blanc +   '|COMPAGNIE |'
CompagniesEauxBAS = Couleur.Blanc +    '| DES EAUX |'
PrixCompagniesEaux = Couleur.Blanc   + '|   $150   |' 


LaBourseHAUT = Couleur.Jaune +         '|   LA     |'
LaBourseBAS = Couleur.Jaune +          '|  BOURSE  |'
PrixLaBourse = Couleur.Blanc   +       '|   $260   |' 


SaintHonoréHAUT = Couleur.Jaune +      '| FAUBOURG |'
SaintHonoréBAS = Couleur.Jaune +       '|  HONORÉ  |'
PrixSaintHonoré = Couleur.Blanc   +    '|   $260   |' 


GareNordHAUT = Couleur.Noire +         '|  GARE DU |'
GareNordBAS = Couleur.Noire +          '|   NORD   |'
PrixGareNord = Couleur.Blanc  +        '|   $200   |'


AvenueHenryMartinHAUT = Couleur.Rouge +'|   HENRY  |'
AvenueHenryMartinBAS = Couleur.Rouge + '|  MARTIN  |'
PrixAvenueHenryMartin = Couleur.Blanc +'|   $240   |' 


MalsherbesHAUT = Couleur.Rouge +       '| BOULEVARD|'
MalsherbesBAS = Couleur.Rouge +        '|MALESHERBE|'
PrixMalsherbes = Couleur.Blanc +       '|   $220   |' 



CaseChance2HAUT = Couleur.Bleu +       '|     ?    |'
CaseChance2BAS = Couleur.Bleu +        '|  CHANCE  |'


MatignonHAUT = Couleur.Rouge +         '|  AVENUE  |'
MatignonBAS = Couleur.Rouge +          '| MATIGNONS|'
PrixMatignons = Couleur.Blanc +        '|   $220   |' 


ParcGratuitHAUT = Couleur.Rouge +      '|    $$$   |'
ParcGratuitBAS = Couleur.Rouge +       '|   PARC   |'


PigaleHAUT = Couleur.Orange +          '|   PLACE  |'
PigaleBAS = Couleur.Orange +           '|  PIGALE  |'
PrixPigale = Couleur.Blanc +           '|   $200   |' 


SaintMichelHAUT = Couleur.Orange +     '| BOULEVARD|'
SaintMichelBAS = Couleur.Orange +      '|  MICHEL  |'
PrixSaintMichel = Couleur.Blanc +      '|   $180   |' 


CaisseCommunautéHAUT = Couleur.Bleu +  '| CAISSE DE|'
CaisseCommunautéBAS = Couleur.Bleu +   '|COMMUNAUTÉ|'


MozartHAUT = Couleur.Orange +          '|  AVENUE  |'
MozartBAS = Couleur.Orange +           '|  MOZART  |'
PrixMozart = Couleur.Blanc +           '|   $180   |' 


GareLyonHAUT = Couleur.Noire +         '|  GARE DE |'
GareLyonBAS = Couleur.Noire +          '|   LYON   |'
PrixGareLyon = Couleur.Blanc  +        '|   $200   |'



ParadisHAUT = Couleur.Violet +         '|  RUE DE  |'
ParadisBAS = Couleur.Violet +          '|  PARADIS |'
PrixParadis = Couleur.Blanc +          '|   $160   |' 


NeuillyHAUT = Couleur.Violet +         '|  RUE DE  |'
NeuillyBAS = Couleur.Violet +          '|  NEUILLY |'
PrixNeuilly = Couleur.Blanc +          '|   $140   |' 


ElectriciteHAUT = Couleur.Blanc +      '| COMPAGNIE|'
ElectriciteBAS = Couleur.Blanc +       '|  LUMIÈRE |'
PrixElectricite = Couleur.Blanc +      '|    $150  |' 


ViletteHAUT = Couleur.Violet +         '| BOULEVARD|'
ViletteBAS = Couleur.Violet +          '|  VILETTE |'
PrixVilette = Couleur.Blanc +          '|    $140  |' 


PrisonHAUT = Couleur.Gris +            '|     LA   |'
PrisonBAS = Couleur.Gris +             '|  PRISON  |'


RepubliqueHAUT = Couleur.Bleu +        '|  AVENUE  |'
RespubliqueBAS = Couleur.Bleu +        '|REPUBLIQUE|'
PrixReplublique = Couleur.Blanc +      '|   $120   |' 


CourcellesHAUT = Couleur.Bleu +        '|  RUE DE  |'
CourcelleBAS = Couleur.Bleu +          '|COURCELLES|'
PrixCourcelle = Couleur.Blanc +        '|   $100   |' 


CaseChanceHAUT = Couleur.Rose +        '|     ?    |'
CaseChanceBAS = Couleur.Rose +         '|  CHANCE  |'
PrixCaseChance = Couleur.Bleu +        '|     ?    |'


VaugirardHAUT = Couleur.Bleu +         '|  RUE DE  |'
VaugirardBAS = Couleur.Bleu +          '|VAUGIRARD |'
PrixVaugirard = Couleur.Blanc +        '|   $100   |' 


GareMontparnasseHAUT = Couleur.Noire + '|  GARE DE |'
GareMontparnasseBAS = Couleur.Noire +  '|MONTPARNAS|'
PrixGareMontparnasse = Couleur.Blanc  +'|   $200   |'


ImpotsRevenuHAUT = Couleur.Blanc+      '|IMPOTS SUR|'
ImpotsRevenusBAS = Couleur.Blanc +     '|LE REVENU |'
PrixImpotsRevenus = Couleur.Blanc  +   '|   $200   |'


LecourbeHAUT = Couleur.Rose +          '|    RUE   |'
LecourbeBAS = Couleur.Rose +           '| LECOURBE |'
PrixLecourbe = Couleur.Blanc +         '|    $60   |' 


CaisseCommunautéHAUT = Couleur.Bleu +  '| CAISSE DE|'
CaisseCommunautéBAS = Couleur.Bleu +   '|COMMUNAUTÉ|'
PrixCaisseCommunauté = Couleur.Bleu +  '|    :)    |'


BellevilleHAUT = Couleur.Rose +        '| BOULEVARD|'
BellevilleBAS = Couleur.Rose +         '|BELLEVILLE|'
PrixBelleville = Couleur.Blanc +       '|    $60   |' 

# Fin creation des cartes


# 1Creation des joueurs
NombreJoueur = int(input("Combien de joueur >> "))
if NombreJoueur > 4:
    Joueur = 'Pok'
    print(Couleur.Rouge + "Il y a trop de joueur :/")
elif NombreJoueur < 2:
    Joueur = 'Pok'
    print(Couleur.Rouge + "Pas assez de joueur :/")

elif NombreJoueur > 1 and NombreJoueur < 5:
    print("Creation des",NombreJoueur,"joueurs")
    Joueur = 'ok'

# 2Creation des joueurs 
if Joueur == 'ok':
    if NombreJoueur == 2:
        NomJoueur1 = input("Prenom du Joueur 1 >> ")
        PlaceP1 = 0
        Propriete1 = []
        Tour1 = 1
        Argent1 = 1500
        NomJoueur2 = input("Prenom du Joueur 2 >> ")
        PlaceP2 = 0
        Propriete2 = []
        Tour2 = 0
        Argent2 = 1500
    elif NombreJoueur == 3:
        NomJoueur1 = input("Prenom du Joueur 1 >> ")
        PlaceP1 = 0
        Propriete1 = []
        Tour1 = 1
        Argent1 = 1500
        NomJoueur2 = input("Prenom du Joueur 2 >> ")
        PlaceP2 = 0
        Propriete2 = []
        Tour2 = 0
        Argent2 = 1500
        NomJoueur3 = input("Prenom du Joueur3 >> ")
        PlaceP3 = 0
        Argent3 = 1500
        Propriete3 = []
        Tour3 = 0
    elif NombreJoueur == 4:
        NomJoueur1 = input("Prenom du Joueur 1 >> ")
        PlaceP1 = 0
        Propriete1 = []
        Tour1 = 1
        Argent1 = 1500
        NomJoueur2 = input("Prenom du Joueur 2 >> ")
        PlaceP2 = 0
        Propriete2 = []
        Tour2 = 0
        Argent2 = 1500
        NomJoueur3 = input("Prenom du Joueur3 >> ")
        PlaceP3 = 0
        Propriete3 = []
        Argent3 = 1500
        Tour3 = 0
        NomJoueur4 = input("Prenom du Joueur 4 >> ")
        PlaceP4 = 0
        Argent4 = 1500
        Propriete4 = []
        Tour4 = 0


# Creation du plateau
def Map():
    print('                                                                              ',     PrisonHAUT,ViletteHAUT, ElectriciteHAUT, NeuillyHAUT, ParadisHAUT, GareLyonHAUT, MozartHAUT, CaisseCommunautéHAUT, SaintMichelHAUT,PigaleHAUT, ParcGratuitHAUT)
    print('                                                                              '      ,PrisonBAS,ViletteBAS,  ElectriciteBAS,  NeuillyBAS,  ParadisBAS,  GareLyonBAS,  MozartBAS,  CaisseCommunautéBAS,  SaintMichelBAS, PigaleBAS, ParcGratuitBAS) 
    print('                                                                                           ', PrixVilette, PrixElectricite, PrixNeuilly, PrixParadis, PrixGareLyon, PrixMozart,'            ',        PrixSaintMichel, PrixPigale)   

    print('                                                                              ',RepubliqueHAUT,'                                                                                                                    ',                  MatignonHAUT)
    print('                                                                              ',RespubliqueBAS,'                                                                                                                    ',                  MatignonBAS)
    print('                                                                              ',PrixReplublique,'                                                                                                                    ',                  PrixMatignons)
   
    print('')
    print('                                                                              ',CourcellesHAUT,'                                                                                                                    ',                  CaseChance2HAUT)
    print('                                                                              ',CourcelleBAS,'                                                                                                                    ',                  CaseChance2BAS)
    print('                                                                              ',PrixCourcelle,'                                                                                                                    ',PrixCaseChance)



    print('')
    print('                                                                              ',CaseChance2HAUT,'                                                                                                                    ',                  MalsherbesHAUT)
    print('                                                                              ',CaseChance2BAS,'                                                                                                                    ',                  MalsherbesBAS)
    print('                                                                              ',CaseChance2HAUT,'                                                                                                                    ',                  PrixMalsherbes)

    print('')
    print('                                                                              ',VaugirardHAUT,'                                                                                                                    ',                  AvenueHenryMartinHAUT)
    print('                                                                              ',VaugirardBAS,'                                                                                                                    ',                  AvenueHenryMartinBAS)
    print('                                                                              ',PrixVaugirard,'                                                                                                                    ',                  PrixAvenueHenryMartin)
   
    print('')
    print('                                                                              ',GareMontparnasseHAUT,'                                                                                                                    ',                  GareNordHAUT)
    print('                                                                              ',GareMontparnasseBAS,'                                                                                                                    ',                  GareNordBAS)
    print('                                                                              ',PrixGareMontparnasse,'                                                                                                                    ',                  PrixGareNord)

    print('                                                                              ')
    print('                                                                              ',ImpotsRevenuHAUT,'                                                                                                                    ',                  SaintHonoréHAUT)
    print('                                                                              ',ImpotsRevenusBAS,'                                                                                                                    ',                  SaintHonoréBAS)
    print('                                                                              ',PrixImpotsRevenus,'                                                                                                                    ',                  PrixSaintHonoré)

    print('                                                                               ')
    print('                                                                              ',LecourbeHAUT,'                                                                                                                    ',                  LaBourseHAUT)
    print('                                                                              ',LecourbeBAS,'                                                                                                                    ',                  LaBourseBAS)
    print('                                                                              ',PrixLecourbe,'                                                                                                                    ',                  PrixLaBourse)

    print('                                                                                ')
    print('                                                                              ',CaisseCommunautéHAUT,'                                                                                                                    ',                  CompagniesEauxHAUT)
    print('                                                                              ',CaisseCommunautéBAS,'                                                                                                                    ',                  CompagniesEauxBAS)
    print('                                                                              ',PrixCaisseCommunauté,'                                                                                                                    ',                  PrixCompagniesEaux)

    print('                                                                                                    ')
    print('                                                                              ',BellevilleHAUT,'                                                                                                                    ',                  FayetteHAUT)
    print('                                                                              ',BellevilleBAS,'                                                                                                                    ',                  FayetteBAS)
    print('                                                                              ',PrixBelleville,'                                                                                                                    ',                  PrixFayette)

    print('                                                                               ')
    print('                                                                              ',     CaseDepartHAUT, RueDeLaPaixHAUT, TaxeDeLuxeHAUT, ChampsElyséeHAUT, CaseChanceHAUT, GareSaintLazareHAUT, CapucinesHAUT,CaisseCommunautéHAUT,FochHAUT, BreteuilHAUT, AllezPrisonHAUT)
    print('                                                                              ',     CaseDepartBAS,  RueDeLaPaixBAS,  TaxeDeLuxeBAS,  ChampsEliséeBAS,  CaseChanceBAS,  GareSaintLazareBAS, CapucineBAS,CaisseCommunautéBAS, FochBAS, BreteuilBAS, AllezPrisonBAS) 
    print('                                                                                           ',PrixRuePaix, PrixTaxeDeLuxe, PrixChampsElysée, '            ',PrixGareSaintLazare,PrixCapucine,'            ', PrixFoch, PrixBreteuil)   

                                        
# Lancement de la partie

if Joueur == 'ok':
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    Map()


# Deplacement des joueurs 1 + gestion carte libre + cout
if Joueur == 'ok':
    Belleville = 1
    BellevilleLibre = True      

    Communauté1 = 2
    
    Lecourbe = 3
    LecourbeLibre = True

    Impots = 4

    Montparnasse = 5
    MontparnasseLibre = True
    
    Vaugirard = 6
    VaugirardLibre = True

    Chance1 = 7

    Courcelles = 8
    Courcelles = True

    Republique = 9
    RepubliqueLibre = True
    Prison = 10
    
    Villette = 11
    VilletteLibre = True
    
    Electricite = 12
    
    Neuilly = 13
    NeuillyLibre = True
    
    Paradis = 14
    ParadisLibre = True

    GareLyon = 15
    GareLyonLibre = True

    Mozart = 16
    MozartLibre = True
    
    Communaute2 = 17

    SaintMichel = 18
    SaintMichelLibre = True
    
    Pigalle = 19
    PigaleLibre = True

    ParcGratuit = 20
    
    Matignon = 21
    MatignonLibre = True
    
    Chance2 = 22

    Malsherbes = 23
    MalsherbesLibre = True

    HenryMartin = 24
    HenryMartinLibre = True

    GareNord = 25
    GareNordLibre = True
    
    SaintHonore = 26
    SaintHonoreLibre = True

    Bourse = 27
    BourseLibre = True

    DistributionEaux = 28

    Fayette = 29
    FayetteLibre = True

    AllezPrison = 30

    Breteuil = 31
    BreteuilLibre = True
    
    Foch = 32
    FochLibre = True
    
    Communaute3 = 33

    Capucine = 34
    CapucineLibre = True
    
    SaintLazare = 35
    SaintLazareLibre = True

    Chance3 = 36
    Elysée = 37
    ElyseeLibre = True

    TaxeLuxe = 38

    RueDeLaPaix = 39
    RueDeLaPaixLibre = True
    
    Depart = 0 
CaisseCommunautéCarte = ['+200$','+10$','+400$','-50$','+100$','+25$','-200$','-100$','+50$','20$']
ChanceCarte = ['+200$','-20$','+100$','-15$','+150','-200$','+400$','+50']
# Deplacement des joueur 2
 # ok 

def FichePersonnage():
    print("Nom :",NomJoueur1)
    print("Cagnotte :",Argent1,"$")
    print("Propriete",Propriete1)
    if Tour1 == 1:
        print("Mon tour : OUI")
    else:
        print("Mon tour : NON")
    
    print('')
    print("Nom :",NomJoueur2)
    print("Cagnotte :",Argent2,"$")
    print("Propriete",Propriete2)
    if Tour2 == 1:
        print("Mon tour : OUI")
    else:
        print("Mon tour : NON")
    print('')

    if NombreJoueur == 3:
        print("Nom :",NomJoueur3)
        print("Cagnotte :",Argent3,"$")
        print("Propriete",Propriete3)
    if Tour3 == 1 and NombreJoueur == 3:
        print("Mon tour : OUI")
        print('')
    elif Tour3 != 1 and NombreJoueur == 3:
        print("Mon tour : NON")
        print('')
    
    if NombreJoueur == 4:
        print("Nom :",NomJoueur3)
        print("Cagnotte :",Argent3,"$")
        print("Propriete",Propriete3)
    if Tour3 == 1 and NombreJoueur == 4:
        print("Mon tour : OUI")
        print('')
    elif Tour3 != 1 and NombreJoueur == 4:
        print("Mon tour : NON")
        print('')

    if NombreJoueur == 4:
        print("Nom :",NomJoueur4)
        print("Cagnotte :",Argent4,"$")
        print("Propriete",Propriete4)
    if Tour4 == 1 and NombreJoueur == 4:
        print("Mon tour : OUI")
        print('')
    elif Tour4 != 1 and NombreJoueur == 4:
        print("Mon tour : NON")
        print('')

Tour3 = 0
Tour4 = 0

# Tour joueur 1
while True:
    if Joueur == 'ok':
        if Tour1 == 1:
            FichePersonnage()
            NombreDès = [1, 2, 3, 4, 5, 6]  
            Dès1 = random.choices(NombreDès)
            Dès2 = random.choices(NombreDès)
            Dès3 = Dès1 + Dès2
            Dès3 = Dès3[0]+Dès3[1]
            PlaceP1 += Dès3
            print(PlaceP1)
            if PlaceP1 > 39:
                PlaceP1 = 0
                PlaceP1 += Dès3 - 1
            if PlaceP1 == 1:
                FichePersonnage()
                if BellevilleLibre == True:
                    AcheterBelleville = input("a :Acheter Belleville $60 ou c: continuer >> ")
                    if AcheterBelleville == 'a':
                        Argent1 -= 60
                        Propriete1 += ['Belleville']
                        BellevilleLibre = False
                        Tour1 = 0
                        FichePersonnage()
                        Tour2 = 1
                        FichePersonnage()
                    elif AcheterBelleville == 'c':
                        Tour1 = 0
                        FichePersonnage()
                        Tour2 = 1

            elif PlaceP1 == 2:
                CommuChoix = random.choices[CaisseCommunautéCarte]
                if CommuChoix == '+200$':
                    print('Erreur de la banque en vôtre faveur recevez +200$')
                    Argent1 += 200
                elif CommuChoix == '10$':
                    print("Vous avez gagné le prix de beauté recever +10$")
                    Argent1 += 10
                elif CommuChoix == '400$':
                    print('Vos investisement en crypto vous rapporte +400$')
                    Argent1 += 400
                elif CommuChoix == '-50$':
                    print('Amende pour excès de vitesse payez -50$')
                    Argent1 -= 50
                elif CommuChoix == '+100$':
                    print("Vos appartement vous rapporte +100$")
                    Argent += 100
                elif CommuChoix == '+25$':
                    print("Vous avez gagné le prix des mots croisées recevez +25$")
                    Argent1 += 25
                elif CommuChoix == '-200$':
                    print("Vous avez payer les impôts payez -200$")
                    Argent -= 200
                elif CommuChoix == '-100$':
                    print('Vous devez payez l\'ecole vous payez -100$')
                    Argent1 -= 100
                elif CommuChoix == '+50$':
                    print("Vous avez obtenue un pourboire de +50$")
                    Argent1 += 50
                elif CommuChoix == '+20$':
                    print('Vous avez eu une promotion vous recevez +20$')
                    Argent1 += 20

            elif PlaceP1 == 3:
                FichePersonnage()
                if LecourbeLibre == True:
                    AcheterLecourbe = input("a :Acheter Lecourbe $60 ou c: continuer >> ")
                    if AcheterLecourbe == 'a':
                        Argent1 -= 60
                        Propriete1 += ['Lecourbe']
                        LecourbeLibre = False
                        Tour1 = 0
                        FichePersonnage()
                        Tour2 = 1
                        FichePersonnage()
                    elif AcheterLecourbe == 'c':
                        Tour1 = 0
                        FichePersonnage()
                        Tour2 = 1

            elif PlaceP1 == 4:
                print("Joueur",NomJoueur1,"est a Impots sur le Revenue")
                Argent -= 200
                FichePersonnage()
                Tour1 = 0
                Tour2 = 1
            
            elif PlaceP1 == 5:
                FichePersonnage()
                if MontparnasseLibre == True:
                    AcheterMontparnasse = input("a :Acheter Lecourbe $60 ou c: continuer >> ")
                    if AcheterMontparnasse == 'a':
                        Argent1 -= 60
                        Propriete1 += ['Montparnasse']
                        MontparnasseLibre = False
                        Tour1 = 0
                        FichePersonnage()
                        Tour2 = 1
                        FichePersonnage()
                    elif AcheterMontparnasse == 'c':
                        Tour1 = 0
                        FichePersonnage()
                        Tour2 = 1
                        
            elif PlaceP1 == 6:
                print("Joueur",NomJoueur1,"est a Rue de Vaugirard")
            elif PlaceP1 == 7:
                print("Joueur",NomJoueur1,"est a Chance")        
            elif PlaceP1 == 8:
                print("Joueur",NomJoueur1,"est a Rue de Courcelles")
            elif PlaceP1 == 9:
                print("Joueur",NomJoueur1,"est a Avenue de la Republique")
            elif PlaceP1 == 10:
                print("Joueur",NomJoueur1,"est a Prison")
            elif PlaceP1 == 11:
                print("Joueur",NomJoueur1,"est a Boulevard de la Villette")  
            elif PlaceP1 == 12:
                print("Joueur",NomJoueur1,"est a Compagnie Distribution Electricite")
            elif PlaceP1 == 13:
                print("Joueur",NomJoueur1,"est a Avenue de Neuilly")
            elif PlaceP1 == 14:
                print("Joueur",NomJoueur1,"est a Rue de Paradis")
            elif PlaceP1 == 15:
                print("Joueur",NomJoueur1,"est a Gare de Lyon")
            elif PlaceP1 == 16:
                print("Joueur",NomJoueur1,"est a Avenue de Mozart")
            elif PlaceP1 == 17:
                print("Joueur",NomJoueur1,"est a Caisse de Communauté")
            elif PlaceP1 == 18:
                print("Joueur",NomJoueur1,"est a Boulevard Saint-Michel")
            elif PlaceP1 == 19:
                print("Joueur",NomJoueur1,"est a Place Pigalle")   
            elif PlaceP1 == 20:
                print("Joueur",NomJoueur1,"est a Parc Gratuit")
            elif PlaceP1 == 21:
                print("Joueur",NomJoueur1,"est a Avenue Matignon")
            elif PlaceP1 == 22:
                print("Joueur",NomJoueur1,"est a Chance")
            elif PlaceP1 == 23:
                print("Joueur",NomJoueur1,"est a Boulevard Malsherbes")
            elif PlaceP1 == 24:
                print("Joueur",NomJoueur1,"est a Avenue Henry-Martin")
            elif PlaceP1 == 25:
                print("Joueur",NomJoueur1,"est a Gare du Nord")
            elif PlaceP1 == 26:
                print("Joueur",NomJoueur1,"est a Faubourg Saint-Honore")
            elif PlaceP1 == 27:
                print("Joueur",NomJoueur1,"est a Place de la Bourse")  
            elif PlaceP1 == 28:
                print("Joueur",NomJoueur1,"est a Compagnie Distribution Eaux")
            elif PlaceP1 == 29:
                print("Joueur",NomJoueur1,"est a Rue la Fayette")
            elif PlaceP1 == 30:
                print("Joueur",NomJoueur1,"est a Allez En Prison")
            elif PlaceP1 == 31:
                print("Joueur",NomJoueur1,"est a Avenue de Breteuil")        
            elif PlaceP1 == 32:
                print("Joueur",NomJoueur1,"est a Avenue Foch")
            elif PlaceP1 == 33:
                print("Joueur",NomJoueur1,"est a Caisse De Communaute")
            elif PlaceP1 == 34:
                print("Joueur",NomJoueur1,"est a Boulevard des Capucines")
            elif PlaceP1 == 35:
                print("Joueur",NomJoueur1,"est a Gare Saint-Lazare")       
            elif PlaceP1 == 36:
                print("Joueur",NomJoueur1,"est a Chance")
            elif PlaceP1 == 37:
                print("Joueur",NomJoueur1,"est a Avenue des Champs Elysées")
            elif PlaceP1 == 38:
                print("Joueur",NomJoueur1,"est a Taxe De Luxe")
            elif PlaceP1 == 39:
                print("Joueur",NomJoueur1,"est a Rue De La Paix") 
            elif PlaceP1 == 0:
                print("Joueur",NomJoueur1,"est a Case Depart")
            Tour1 = 0
            Tour2 = 1

        if Tour1 == 2:
            NombreDès = [1, 2, 3, 4, 5, 6]  
            Dès1 = random.choices(NombreDès)
            Dès2 = random.choices(NombreDès)
            Dès3 = Dès1 + Dès2
            Dès3 = Dès3[0]+Dès3[1]
            PlaceP2 += Dès3
            print(PlaceP2)
            if PlaceP2 > 39:
                PlaceP2 = 0
                PlaceP2 += Dès3 - 1
            if PlaceP2 == 1:
                print("Joueur",NomJoueur2,"est a Belleville")
            elif PlaceP2 == 2:
                print("Joueur",NomJoueur2,"est a Caisse de Communauté")
            elif PlaceP2 == 3:
                print("Joueur",NomJoueur2,"est a Lecourbe")        
            elif PlaceP2 == 4:
                print("Joueur",NomJoueur2,"est a Impots sur le Revenue")
            elif PlaceP2 == 5:
                print("Joueur",NomJoueur2,"est a Gare Montparnasse")
            elif PlaceP2 == 6:
                print("Joueur",NomJoueur2,"est a Rue de Vaugirard")
            elif PlaceP2 == 7:
                print("Joueur",NomJoueur2,"est a Chance")    
            elif PlaceP2 == 8:
                print("Joueur",NomJoueur2,"est a Rue de Courcelles")
            elif PlaceP2 == 9:
                print("Joueur",NomJoueur2,"est a Avenue de la Republique")
            elif PlaceP2 == 10:
                print("Joueur",NomJoueur2,"est a Prison")
            elif PlaceP2 == 11:
                print("Joueur",NomJoueur2,"est a Boulevard de la Villette") 
            elif PlaceP2 == 12:
                print("Joueur",NomJoueur2,"est a Compagnie Distribution Electricite")
            elif PlaceP2 == 13:
                print("Joueur",NomJoueur2,"est a Avenue de Neuilly")
            elif PlaceP2 == 14:
                print("Joueur",NomJoueur2,"est a Rue de Paradis")
            elif PlaceP2 == 15:
                print("Joueur",NomJoueur2,"est a Gare de Lyon")   
            elif PlaceP2 == 16:
                print("Joueur",NomJoueur2,"est a Avenue de Mozart")
            elif PlaceP2 == 17:
                print("Joueur",NomJoueur2,"est a Caisse de Communauté")
            elif PlaceP2 == 18:
                print("Joueur",NomJoueur2,"est a Boulevard Saint-Michel")
            elif PlaceP2 == 19:
                print("Joueur",NomJoueur2,"est a Place Pigalle")    
            elif PlaceP2 == 20:
                print("Joueur",NomJoueur2,"est a Parc Gratuit")
            elif PlaceP2 == 21:
                print("Joueur",NomJoueur2,"est a Avenue Matignon")
            elif PlaceP2 == 22:
                print("Joueur",NomJoueur2,"est a Chance")
            elif PlaceP2 == 23:
                print("Joueur",NomJoueur2,"est a Boulevard Malsherbes")        
            elif PlaceP2 == 24:
                print("Joueur",NomJoueur2,"est a Avenue Henry-Martin")
            elif PlaceP2 == 25:
                print("Joueur",NomJoueur2,"est a Gare du Nord")
            elif PlaceP2 == 26:
                print("Joueur",NomJoueur2,"est a Faubourg Saint-Honore")
            elif PlaceP2 == 27:
                print("Joueur",NomJoueur2,"est a Place de la Bourse")        
            elif PlaceP2 == 28:
                print("Joueur",NomJoueur2,"est a Compagnie Distribution Eaux")
            elif PlaceP2 == 29:
                print("Joueur",NomJoueur2,"est a Rue la Fayette")
            elif PlaceP2 == 30:
                print("Joueur",NomJoueur2,"est a Allez En Prison")
            elif PlaceP2 == 31:
                print("Joueur",NomJoueur2,"est a Avenue de Breteuil")        
            elif PlaceP2 == 32:
                print("Joueur",NomJoueur2,"est a Avenue Foch")
            elif PlaceP2 == 33:
                print("Joueur",NomJoueur2,"est a Caisse De Communaute")
            elif PlaceP2 == 34:
                print("Joueur",NomJoueur2,"est a Boulevard des Capucines")
            elif PlaceP2 == 35:
                print("Joueur",NomJoueur2,"est a Gare Saint-Lazare")        
            elif PlaceP2 == 36:
                print("Joueur",NomJoueur2,"est a Chance")
            elif PlaceP2 == 37:
                print("Joueur",NomJoueur2,"est a Avenue des Champs Elysées")
            elif PlaceP2 == 38:
                print("Joueur",NomJoueur2,"est a Taxe De Luxe")
            elif PlaceP2 == 39:
                print("Joueur",NomJoueur2,"est a Rue De La Paix")        
            elif PlaceP2 == 0:
                print("Joueur",NomJoueur2,"est a Case Depart")
                
            Tour2 = 0
            Tour1 = 1
        








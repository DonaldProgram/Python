# chatBot
import unidecode

# base dans laquelle le bot va chercher la reponse
base_Donne = {
    "comment sa va" : "BOT- Sa va :) Merci !",
    "bonjour"       : "BOT- Bonjour, je m'appele BOT."
                }

DerniereReponseBOT = "rien"
nbMessage = 0

while True:
    print("")
    # Recupere ce que l'humain veut dire puis enleve les accents et les majuscules
    texteHUMAIN = input("VOUS- ")
    nbMessage += 1
    texteHUMAINremake = unidecode.unidecode(texteHUMAIN)
    texteHUMAIN = texteHUMAINremake.lower()

    # le bot lui reponds
    
    if 'bonjour' in texteHUMAIN or 'salut' in texteHUMAIN or 'comment tu t\'appele' in texteHUMAIN or 'quel est ton nom' in texteHUMAIN:
        if DerniereReponseBOT == "rien":
            print(base_Donne["bonjour"]) # repond 'Bonjour je m'appele BOT'
            DerniereReponseBOT = "debut"
        else:
            print("BOT- Je ne pense pas que ce soit le bon moment pour que je te le dises.")


    elif 'comment tu va' in texteHUMAIN or 'comment sa va' in texteHUMAIN or 'sa va' or 'comment tu te sens' in texteHUMAIN:
        print(base_Donne["comment sa va"]) # repond sa va merci
    
    else:
        print("BOT- Desoler, on ne ma pas encore appris a faire cela.")

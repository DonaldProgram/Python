# chatBot
import unidecode

# base dans laquelle le bot va chercher la reponse
base_Donne = {
    "presentation"       : "BOT- Bonjour, je m'appele BOT. Je suis heureux de vous rencontrer.",
    "comment sa va"      : "BOT- Sa va :) Merci !",
    "pas appris"        : "BOT- Desoler je n'ai pas compris. Qu'auriez vous repondue"
             }

DerniereReponseBOT = "rien"
nbMessage = 0

print("Ne repond pas si trop de faute d'orthographe et ne pas mettre de point ou de virgule")




while True:
    print("")
    # Recupere ce que l'humain veut dire puis enleve les accents et les majuscules
    texteHUMAIN = input("VOUS- ")
    nbMessage += 1
    texteHUMAINremake = unidecode.unidecode(texteHUMAIN)
    texteHUMAIN = texteHUMAINremake.lower()

    if texteHUMAIN == "bonjour" or texteHUMAIN == "bonjour " or texteHUMAIN == "salut " or texteHUMAIN == "salut" or texteHUMAIN == "comment tu t'appele" or texteHUMAIN == "comment tu t'appele " or texteHUMAIN == "quel est ton nom" or texteHUMAIN == "quel est ton nom ":
        print(base_Donne["presentation"])
        
    else:
        print(base_Donne["pas appris"])

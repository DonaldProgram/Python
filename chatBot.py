# chatBot
import unidecode

# base dans laquelle le bot va chercher la reponse
base_Donne = {
    "presentation"       : "BOT- Bonjour, je m'appele BOT. Je suis heureux de vous rencontrez.",
    "comment sa va"      : "BOT- Sa va :) Merci !",
    "pas appris"        : "BOT- Desoler je n'ai pas compris :("
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
        

    elif texteHUMAIN in base_Donne:
        print(base_Donne[texteHUMAIN])

    # demande ce que le joueur aurais repondu
    else:
        print("")
        print(base_Donne["pas appris"])
        print("BOT- Qu'auriez vous repondu(e) a ma place ?, pour que je puisse l'ajouter à ma base de donné.")
        ajoutBaseDonne = input("BOT- Si vous ne savez pas vous pouvez me le dire (je ne sais pas) : ")
        ajoutBaseDonneRemake = unidecode.unidecode(ajoutBaseDonne)
        ajoutBaseDonne = ajoutBaseDonneRemake.lower()

        if ajoutBaseDonne == "je ne sais pas" or ajoutBaseDonne == "je ne sais pas " or ajoutBaseDonne == "aucune idee":
            print("BOT- Ce n'est pas grave moi non plus je n'ai pas reussis a repondre.")
        else:
            print("")
            base_Donne[texteHUMAIN] = ajoutBaseDonne
            print("BOT- Merci de cet ajout dans ma base de donne je la ferais traiter pour voir si elle est bien bonne.")

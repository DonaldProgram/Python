# chatBot
import unidecode

# base dans laquelle le bot va chercher la reponse
base_Donne = {
    "presentation"       : "BOT- Bonjour, je m'appele BOT. Je suis heureux de vous rencontrez.",
    "comment sa va"      : "BOT- Sa va :) Merci !",
    "pas appris"         : "BOT- Desoler je n'ai pas compris :(",
    "prenom_User"        : "BOT- Genial, j'aimerais beaucoup avoir un prenom comme le tien.",
    "age_user"           : "BOT- C'est super comme age, moi aussi j'ai un age c'est 1 car je suis le 'NUMERO UNO'" 
             }


reponse = 0

print("Ne repond pas si trop de faute d'orthographe et ne pas mettre de point ou de virgule")

while True:
    print("")
    # Recupere ce que l'humain veut dire puis enleve les accents et les majuscules
    texteHUMAIN = input("VOUS- ")
    texteHUMAINremake = unidecode.unidecode(texteHUMAIN)
    texteHUMAIN = texteHUMAINremake.lower()

    # repond a bonjour
    if texteHUMAIN == "bonjour" or texteHUMAIN == "bonjour " or texteHUMAIN == "salut " or texteHUMAIN == "salut" or texteHUMAIN == "comment tu t'appele" or texteHUMAIN == "comment tu t'appele " or texteHUMAIN == "quel est ton nom" or texteHUMAIN == "quel est ton nom " or texteHUMAIN == "hello" or texteHUMAIN == "hello ":
        print(base_Donne["presentation"])
        reponse = 1

    # repond a comment sa va
    if texteHUMAIN == "comment sa va" or texteHUMAIN == "comment sa va " or texteHUMAIN == "comment tu te sens" or texteHUMAIN == "comment tu te sens " or texteHUMAIN == "sa va" or texteHUMAIN == "sa va ":
        print(base_Donne["comment sa va"])
        reponse = 1

    # repond a je m'appele ... de l'utilisateur
    if "je m'appele" in texteHUMAIN or "mon prenom est" in texteHUMAIN or "je suis" in texteHUMAIN or "mon nom est" in texteHUMAIN:
        print(base_Donne["prenom_User"])
        reponse = 1

    # repond a mon age est ...
    if "j'ai" and "ans" in texteHUMAIN:
        print(base_Donne["age_user"])
        reponse = 1



    if reponse == 0:
        if texteHUMAIN in base_Donne:
            print(base_Donne[texteHUMAIN])
            reponse = 1



    # demande ce que le joueur aurais repondu
    if reponse == 0:
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

            base_Donne[texteHUMAIN] = "BOT- " + ajoutBaseDonne
            print("BOT- Merci de cet ajout dans ma base de donne je la ferais traiter pour voir si elle est bien bonne.")

    reponse = 0

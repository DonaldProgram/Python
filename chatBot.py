# chatBot
import unidecode
from datetime import *

reponse = 0

print("Ne repond pas si trop de faute d'orthographe et ne pas mettre de point ou de virgule")

while True:
    # base de donne dans laquelle le bot va chercher les reponses
    base_Donne = {
    "presentation"       : "BOT- Bonjour, je m'appele BOT. Je suis heureux de vous rencontrez.",
    "comment sa va"      : "BOT- Sa va :) Merci !",
    "pas appris"         : "BOT- Desoler je n'ai pas compris :(",
    "prenom_User"        : "BOT- Genial, j'aimerais beaucoup avoir un prenom comme le tien.",
    "age_user"           : "BOT- C'est super comme age, moi aussi j'ai un age c'est 1 car je suis le 'NUMERO UNO'.",
    "maisonBOT"          : "BOT- Je vis dans une ville paisible aussi appelé ordinateur.",
    "heure"              : "BOT- Il est " + datetime.now().strftime("%H:%M:%S") + ".",
    "jour-mois"          : "BOT- Nous somme le " + datetime.now().strftime('%d-%m-%Y') + "."
             }
    print("")
    # Recupere ce que l'humain veut dire puis enleve les accents et les majuscules
    texteHUMAIN = input("VOUS- ")
    texteHUMAINremake = unidecode.unidecode(texteHUMAIN)
    texteHUMAIN = texteHUMAINremake.lower()

    # repond a bonjour
    if reponse == 0:
        if texteHUMAIN == "bonjour" or texteHUMAIN == "bonjour " or texteHUMAIN == "salut " or texteHUMAIN == "salut" or texteHUMAIN == "comment tu t'appele" or texteHUMAIN == "comment tu t'appele " or texteHUMAIN == "quel est ton nom" or texteHUMAIN == "quel est ton nom " or texteHUMAIN == "hello" or texteHUMAIN == "hello " or "qui es tu" in texteHUMAIN:
            print(base_Donne["presentation"])
            reponse = 1

    # repond a comment sa va
    if reponse == 0:
        if "comment" and "va" in texteHUMAIN or "comment" and "tu" and "sens" in texteHUMAIN or "sa va" in texteHUMAIN or "quelle est ton humeur" in texteHUMAIN:
            print(base_Donne["comment sa va"])
            reponse = 1

    # repond a je m'appele ... de l'utilisateur
    if reponse == 0:
        if "je m'appele" in texteHUMAIN or "mon prenom est" in texteHUMAIN or "mon nom est" in texteHUMAIN:
            print(base_Donne["prenom_User"])
            reponse = 1

    # repond a mon age est ...
    if reponse == 0:
        if "j'ai" and "ans" in texteHUMAIN or "mon age est" in texteHUMAIN or 'je vais avoir' and "ans" in texteHUMAIN or "j'ai eu" and "ans" in texteHUMAIN:
            print(base_Donne["age_user"])
            reponse = 1
    
    # repond a ou tu habites
    if reponse == 0:
        if "ou tu habite" in texteHUMAIN or "ou vis tu" in texteHUMAIN or "ou habite tu" in texteHUMAIN or "habite tu" in texteHUMAIN or "ou est ce que tu habites" in texteHUMAIN:
            print(base_Donne["maisonBOT"])
            reponse = 1

    # repond a heure
    if reponse == 0:
        if "quelle heure" in texteHUMAIN or "a tu l'heure" in texteHUMAIN or "heure" in texteHUMAIN:
            print(base_Donne["heure"])
            reponse = 1

    # repond a quelle jour
    if reponse == 0:
        if "quelle jour" in texteHUMAIN:
            print(base_Donne["jour-mois"])
            reponse = 1





    # cherche dans la base de donne
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
        ajoutBaseDonneRemake2 = ajoutBaseDonneRemake.lower()

        if ajoutBaseDonneRemake2 == "je ne sais pas" or ajoutBaseDonneRemake2 == "je ne sais pas " or ajoutBaseDonneRemake2 == "aucune idee":
            print("BOT- Ce n'est pas grave moi non plus je n'ai pas reussis a repondre.")
        else:
            print("")

            base_Donne[texteHUMAIN] = "BOT- " + ajoutBaseDonne
            print("BOT- Merci de cet ajout dans ma base de donne je la ferais traiter pour voir si elle est bien bonne.")

    reponse = 0

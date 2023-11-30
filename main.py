import random
import characters
import getpass

print("*** Bienvenu dans le jeu dual fight ***\n")

jedi_user_name = input("veuillez entrer le nom de votre avatar\nreponse : ")
jedi_sexe  = input("quel est votre sexe ?(M/F)\nreponse : ")
jedi = characters.character(jedi_user_name,jedi_sexe,50, 5,15, 3,"gauche",1)
characters.welcome_message(jedi)


ith_user_name = input("veuillez entrer le nom de votre avatar\nreponse : ")
sith_sexe  = input("quel est votre sexe ?(M/F)\nreponse : ")
sith = characters.character(ith_user_name,sith_sexe,100, 5,15, 0,"droit",1)
characters.welcome_message(sith)

print("\nMedames et messieur bienvenus dans l'arene du dual fight. Ce soir : \n".upper())
characters.Introduction(jedi)
characters.Introduction(sith)

print("Voici les mecaniques du jeu".upper())
print("A  chaque tour, vous pouvez choisir entre 0,1, et 2")
print("avec 0 vous pouvez rester passif  et vous gagnez un point (1) d'endurance mais vous prenez de plein fouet le coup enemi. ")
print("Avec 1, vous optez pour une defense qui vous permet d'encaiiser le coup enemie sans perdre en point de vie mais vous perdez O.5 points en endurance ")
print("Avec 2, vous optez pour une attaque dont le force sera compris au hazard entre la valeur de frappe minimale et maximale de votre avatar")
print("le premier a O point de vie aura perdu le combat")



while characters.is_alive(jedi) and characters.is_alive(sith) :
    while jedi.choice != "0" and jedi.choice != "1" and jedi.choice != "2" :
        jedi.choice = getpass.getpass("que choisis "+str(jedi.name)+" ?\n reponse :")
    while sith.choice != "0" and sith.choice != "1" and sith.choice != "2":
        sith.choice = getpass.getpass("que choisis "+str(sith.name)+"?\n reponse :")
    jedi.choice = int(jedi.choice)
    sith.choice = int(sith.choice)
    if jedi.choice == 0 and sith.choice == 0:
        characters.passivity(jedi)
        characters.passivity(sith)
        characters.health_printer(jedi,sith)
    elif jedi.choice == 0 and sith.choice == 1:
        characters.passivity(jedi)
        characters.defense(sith,jedi)
        characters.health_printer(jedi,sith)
    elif jedi.choice == 0 and sith.choice == 2:
        characters.passivity(jedi)
        characters.strike(sith,jedi)
        characters.health_printer(jedi,sith)


    elif jedi.choice == 1 and sith.choice == 0:
        characters.defense(jedi,sith)
        characters.passivity(sith)
        characters.health_printer(jedi,sith)

    elif jedi.choice == 1 and sith.choice == 1:
        characters.defense(jedi, sith)
        characters.defense(sith, jedi)
        characters.health_printer(jedi,sith)

    elif jedi.choice == 1 and sith.choice == 2:
        #characters.strike(sith,jedi)
        characters.defense_against_strike(jedi,sith)
        characters.health_printer(jedi,sith)


    elif jedi.choice == 2 and sith.choice == 0:
            characters.strike(jedi,sith)
            characters.passivity(sith)
            characters.health_printer(jedi, sith)

    elif jedi.choice == 2 and sith.choice == 1:
        characters.defense_against_strike(sith, jedi)
        characters.health_printer(jedi,sith)

    elif jedi.choice == 2 and sith.choice == 2:
        characters.strike(jedi,sith)
        characters.strike(sith,jedi)
        characters.health_printer(jedi,sith)

print("\n*** fin du jeu ***\n")
import characters
import getpass
import shutil

def center_text(text):
    terminal_width, _ = shutil.get_terminal_size()

    # Calcul de l'espacement nécessaire pour centrer le texte
    padding = (terminal_width - len(text)) // 2

    # Affichage du texte centré avec l'espacement calculé
    print(" " * padding + text)

# Utilisation
center_text("***fight club ***\n".upper())
center_text("Bienvenue dans l'arene du FIGHT CLUB.")
center_text("Ne paniquez pas. vous vous demandez surement ce que vous faites ici non ?")
center_text("et bien vous etes ici pour divertir. OUI, Divertir. ")
center_text("ce soir, l'elite de notre pays s'est rassemblé pour vous voir leur offir du divertissement senglant et mortel")
center_text("avant vous etiez des hommes libres vivant librement. Mais aujourd'hui vous etes les prisoniers du FIGHT CLUB et le seul moyen de retrouver votre liberté est de...")
center_text("TUER")
center_text("TUER votre adversaire")
center_text("Vous avez bien compris. Un combat a mort dont le seul survivant pourra sortir d'ici couvert de richesses et le perdant finira juste six pieds sous terre.")
center_text("Ah oui j'avais oublié. Je suis impardonable. Je suis Gravik le seul et l'unique présentateur de cette soirée. ")
center_text("Et vous mes chers combatabts qui etes vous ?")

jedi_user_name = input("Quel est votre nom ?\nreponse : ")
jedi_sexe  = input("ca peut paraitre indiscret "+jedi_user_name+" mais quel est votre sexe ? On ne sait plus trop qui est qui aujourd'hui\nreponse (M:masulin/F:feminin): ").capitalize()
while jedi_sexe != "M" and jedi_sexe != "F":
    jedi_sexe = input(jedi_user_name+" CHOISIS ENTRE UN HOUMME OU UNE FEMME. (M/m pour masculin  ou F/f pour feminin.)\nquel est votre sexe ?(M/F)\nreponse : ").capitalize()

jedi = characters.character(jedi_user_name,jedi_sexe,50, 5,15, characters.side[0],10,None)

sith_health = 50
sith_user_name = input("Et vous dans l'autre coin, quel est votre nom ?\nreponse : ")
sith_sexe  = input(sith_user_name+" quel est votre sexe ?(M/F)\nreponse : ").capitalize()
while sith_sexe != "M" and sith_sexe != "F":
    sith_sexe = input(sith_user_name+" CHOISIS ENTRE UN HOUMME OU UNE FEMME. (M pour masculin  ou F pour feminin.)\nquel est votre sexe ?(M/F)\nreponse : ").capitalize()

sith = characters.character(sith_user_name,sith_sexe,sith_health, 5,15, characters.side[1],10,None)

print("Pour pimenter le combat, nous avons decider de vous donner un choix.")
print("Un choix entre deux drogues. la premiere augmente votre santé de 10% et l'autre votre endurance de 10% aussi")
characters.drug_choice(jedi)
characters.drug_choice(sith)

print("\nMedames et messieur bienvenus dans l'arene du fight club . Ce soir : \n".upper())
characters.Introduction(jedi)
characters.Introduction(sith)

print("Bienvenue dans le jeu Fight Club !".upper())
print("Voici les regles :")
print("Dans chaque tour, vous pouvez choisir parmi les options 0, 1 et 2.")
print("En choisissant 0, vous restez passif, gagnant ainsi 1 point d'endurance, mais vous prenez le coup de l'ennemi en pleine face.")
print("En choisissant 1, vous optez pour la défense, vous permettant d'encaisser le coup sans perdre de points de vie, mais vous perdez 0,5 points d'endurance.")
print("En choisissant 2, vous choisissez l'attaque, infligeant des dégâts aléatoires entre la valeur minimale et maximale de la force de votre avatar.")
print("Le premier joueur à atteindre 0 point de vie perd le combat.")


while characters.is_alive(jedi) and characters.is_alive(sith) :
    while jedi.choice != "0" and jedi.choice != "1" and jedi.choice != "2" :
        jedi.choice = getpass.getpass("Que choisis "+str(jedi.name)+" ?\n reponse :")
    while sith.choice != "0" and sith.choice != "1" and sith.choice != "2":
        sith.choice = getpass.getpass("Que choisis "+str(sith.name)+"?\n reponse :")
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
print("\n*** fin du jeu ***\n".upper())
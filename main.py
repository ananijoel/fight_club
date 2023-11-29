import random
import characters
print("*** Bienvenu dans le jeu dual fight ***\n")
# definition et instanciation des propiétés de l'objet du premier user
#jedi_user_name = input("veuillez entrer le nom de votre avatar\nreponse : ")
#jedi_sexe  = input("quel est votre sexe ?(M/F)\nreponse : ")
jedi = characters.character("joel", "M", 100, 10, 3,"gauche")
# message d'acceuil pour le premier user
characters.welcome_message(jedi)

# definition et instanciation des propiétés de l'objet du second user
#sith_user_name = input("veuillez entrer le nom de votre avatar\nreponse : ")
#sith_sexe  = input("quel est votre sexe ?(M/F)\nreponse : ")
sith = characters.character("elie", "F", 150, 15, 0,"droit")
# message d'acceuil pour le second user
characters.welcome_message(sith)

print("Medames et messieur bienvenus dans l'arene du dual fight. Ce soir : \n".upper())

characters.Introduction(jedi)

characters.Introduction(sith)

"""
while characters.is_alive(jedi) and characters.is_alive(sith):
    user_choice = input("souhaitez vous attaquer (1) ou utiliser une potion (2) ? \nreponse : ")
    if user_choice.isdigit() and int(user_choice) == 1:
        characters.strike(jedi,sith)
        characters.strike(sith,jedi)
    elif user_choice.isdigit() and int(user_choice) == 2:
        characters.healing(jedi)
        characters.strike(sith,jedi)

if characters.is_alive(jedi) :
    print("vous avez gagné\nFelicitations!!")
else:
    print("vous avez perdu\nGros LOOSER")
"""
import random
import characters
print("*** Bienvenu dans le jeu dual fight ***\n")
user_name = input("veuillez entrer le nom de votre avatar\nreponse : ")
sexe  = input("quel est votre sexe ?(M/F)\nreponse : ")
jedi = characters.character(user_name,sexe, 100,10, 3)
sith = characters.character("dark vador","M",150,15,0,)
characters.welcome_message(jedi)

print("vous allez affronter "+sith.name+"\n")
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
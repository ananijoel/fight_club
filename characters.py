import random
#import main

 #TODO
 # capitaliser le sexe pour ne plus avoir a faire une double verification sur le if

class character :
    def __init__(self, name, sexe, health, min_strength,max_strength, number_of_health_potion, side, endurance, choice=None):
        self.name = name.capitalize()
        self.sexe = sexe
        self.health = health
        self.min_strength = min_strength
        self.max_strength = max_strength
        self.number_of_health_potion  = number_of_health_potion
        self.is_alive = is_alive
        self.side = side
        self.endurance = endurance
        self.choice = choice
        if self.sexe == "M":
            self.sexe = "il"
        elif self.sexe == "F":
            self.sexe = "elle"


def is_alive(character) :
    if character.health > 0:
        character.is_alive = True
        return character.is_alive
    else:
        character.is_alive = False
        return character.is_alive

def Introduction(character) :
    print("Dans le coin "+str(character.side)+" du ring nous avons :")
    print(character.name + " avec une force de frappe maxiamle de " + str(character.max_strength) + " points.")
    print("Et une santé s'elevant a " + str(character.health) + " points\n")

def endurance_state(character):
    passif = 1
    defense = 0.5
    actif = 1
    if character.choice == 0 :
        character.endurance += passif
    elif character.choice  == 1 :
        character.endurance -= defense
    elif character.choice == 2 :
        character.endurance -= actif


def welcome_message(character) :
    if character.sexe == "M"  or character.sexe == "m" :
        print("bienvenu sir "+character.name)
    elif character.sexe == "F" or character.sexe == "f" :
        print("bienvenu dame "+character.name)
def healing(character):
    if character.number_of_health_potion > 0:
        potion_effect = random.randrange(1,15)
        character.health = character.health + potion_effect
        character.number_of_health_potion = character.number_of_health_potion -1
        print(str(character.name)+"a utilisé une potion. Il a gagné "+str(potion_effect)+" de point de vie. Il a maintenant "+str(character.health)+" de point de vie ")
    else:
        print("vous n'avez plus de potion")

def strike(character,character_2):
    endurance_state(character)
    if character.endurance >= 0 :
        damage = random.randrange(character.min_strength, character.max_strength)
        character_2.health = character_2.health - damage
        print("----------------")
        print(str(character.name)+" a infligé "+str(damage)+" de degat a "+str(character_2.name))
        print(str(character.name) + " a perdu 1 de son endurance. Maintenant, son endurance est de " + str(character.endurance))
    else :
        character.endurance = 0
        print(str(character.name)+" n'a plus assez d'endurance pour defendre")


def defense (character,character_2) :
    endurance_state(character)
    if character.endurance >= 0 :
        print("----------------")
        print(str(character.name) + " a choisi la defense.")
        print(str(character.name) + " a perdu 0.5 de son endurance. Maintenant, son endurance est de " + str(character.endurance))
        print(str(character.name)+" n'a recu aucun degat pv = "+str(character.health)+"\n")
    else :
        character.endurance = 0
        print(str(character.name)+" n'a plus assez d'endurance pour defendre")
def defense_against_strike(character,character_2) :
    endurance_state(character)
    endurance_state(character_2)
    if character.endurance >= 0 :
        print("----------------")
        print(str(character.name) + " a choisi la defense.")
        print(str(character.name) + " a perdu 0.5 de son endurance. Maintenant, son endurance est de " + str(character.endurance))
        print(str(character_2.name)+" a attaqué "+str(character.name)+" ")
        print(str(character_2.name)+" a perdu 1 point de son endurance. Maintenant, son endurance est de " + str(character_2.endurance))
        print(str(character.name)+" n'a recu aucun degat pv = "+str(character.health)+"\n")
    else:
        character.endurance =0
        strike(character_2,character)
        defense(character,character_2)


def passivity(character):
    endurance_state(character)
    print("----------------")
    print(str(character.name) + " a choisi la passivité.")
    print(str(character.name) + " a gagné 1 d'endurance. Maintenant, son endurance est de " + str(character.endurance))
def health_printer(character,character_2):

    if is_alive(character) and is_alive(character_2) :
        print("*** Etat des joueurs a la fin du tour ***")
        print(str(character.name)+" a "+str(character.health)+" de point de vie restant")
        print(str(character_2.name) + " a " + str(character_2.health) + " de point de vie restant")
        print("*************************************************************************")


    elif is_alive(character) and not is_alive(character_2) :
        print(str(character.name)+" a gagné")
        print("*************************************************************************")

    elif  not is_alive(character) and is_alive(character_2) :
        print(str(character_2.name) + " a gagné")
        print("*************************************************************************")

    elif not is_alive(character) and  not is_alive(character_2):
        print("Match null")
        print("*************************************************************************")

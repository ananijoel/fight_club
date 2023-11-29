import random
class character :
    def __init__(self,name,sexe,health,strength,number_of_health_potion):
        self.name = name
        self.sexe = sexe
        self.health = health
        self.strength = strength
        self.number_of_health_potion  = number_of_health_potion
        self.is_alive = is_alive
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


def welcome_message(character) :
    if character.sexe == "M":
        print("bienvenu sir "+character.name)
    elif character.sexe == "F" :
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
    damage = random.randrange(0, character.strength)
    character_2.health = character_2.health - damage
    if character.health > 0  and character_2.health > 0:
        print(str(character.name)+" a infligé "+str(damage)+" de degat a "+str(character_2.name)+" "+str(character.sexe)+" a maintenant  "+str(character_2.health)+" de points de vie")
    elif  character.health > 0  and character_2.health < 0:
        print(str(character.name)+" a infligé "+str(damage)+" de degat a "+str(character_2.name)+" il a maintenant 0 de points de vie ")
    elif character.health < 0  and character_2.health >  0:
        print(str(character.name) + " a infligé " + str(damage) + " de degat a " + str(character_2.name) + " il a maintenant "+str(character_2.health)+" de points de vie ")
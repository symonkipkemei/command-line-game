
import random


habitat = {1:"front_door",2:"right_door",3:"left_door",4:"central_door",5:"exit_door"}
collection = {"sword":0, "key" : 0, "gun":0, "banana":0}


a = collection.keys()
print(a)

class Opponent:
    """Generate a game play when one enters a door with an opponent
    """

    def __init__(self,name, habitat, strength) -> None:
        """create instance variables
        """
        self.name = name
        self.habitat = habitat
        self.strength = strength
        

class Hero:
    "Generates a gameplay of the hero"

    def __init__(self,name,arsenal) -> None:
        self.name = name
        self.arsenal = arsenal

    def collect(self, item):
        print(f"\nYou have found a {item}!")
        print("****************")
        print("(1).Take it\n(2).Leave it")
        print("****************")
        user_option = int(input("Your choice: "))
        if user_option == 1:
            if item in self.arsenal.keys():
                self.arsenal[item] += 1

        

    def attack(self, other):

        #if the hero wins he has an option of collecting  inventory item

        options = [self.name, other.name]
        choice = random.choice(options) 
        print(choice)
       
        if choice  == self.name:
            print(f"Congratulations {self.name},  won!")

            collect = True
        else:
            print(f"{other.name} defeated you!")
            collect = False
        return collect


class Habitat:
    "maps the environment of the play"

    def __init__(self,name,collection) -> None:
        self.name = name
        self.collection = collection

    def interact_with(self, Opponent,Hero):
        print("\nOptions:\n**************\n(1).Interact further\n(2).Run to the previous room\n**************")
        self.interact_option = int(input("Your choice: "))
        
        if self.interact_option == 1:
            print(f"\nOptions:\n**************\n(1).Fight {Opponent.name}\n(2).Run to the previous room\n**************")
            self.fight_option = int(input("Your choice: "))
            if self.fight_option == 1:
                hero_win = Hero.attack(Opponent)
                if hero_win == True:
                    Hero.collect(self.collection)

            elif self.fight_option == 2:
                exit = True
            else:
                print("wrong input")
        elif self.interact_option == 2:
            exit = True
        else:
            print("wrong input")

            
    def __str__(self) -> str:
        return f"Welcome to the land of milk and war \nAt {self.name} we love vistors. Battles happen and sometime warriors die "
        
        
#habitats
#note that all environments are similar give them properties that makes it different for each
front_door = Habitat("Namibia",collection="spear")
right_door = Habitat("Bostwana",collection="Gun")
left_door = Habitat("Malawi",collection="Grenade")
back_door = Habitat("Kenya",collection="Machette")
exit_door = Habitat("Tanzania",collection=None)

#opponents
black_panther = Opponent("Black panther","On land",5)
gorilla =Opponent("gorilla","forest",4)
prey_mantis =Opponent("Prey Mantis","trees",3)


#Hero
warrior = Hero("symon",arsenal=collection)


# display door options available
def door_choices(*args) -> int:
    """Allows the player to make a choice between the available doors:
    Returns:
        int: the key pair of the chosen door
    """
    #easily retrieve door names using dictionaries keys
    opt ={}
    print()
    for index, x in enumerate(args, 1):
        opt[index] = x
        print(f"{index}. {x}")
    door_choice = input("\nMake your choice:")
    print("\n")
    if door_choice.isdigit():
            door_choice = int(door_choice)
    else:
        print("the option is not available,try again")
    return opt[door_choice]



# the player has an option of entering a new environment and existing

try_again = True

while try_again:
    # display the arsenals in possesion by the player

    print(warrior.arsenal)

    selection = door_choices(front_door.name,right_door.name,left_door.name,back_door.name,exit_door.name)

    print(warrior.arsenal)

    if selection == front_door.name:
        front_door.interact_with(black_panther,warrior)

    elif selection == right_door.name:
        right_door.interact_with(gorilla,warrior)

    elif selection == left_door.name:
        left_door.interact_with(prey_mantis,warrior)

    elif selection ==  exit_door.name:
        try_again = False
        print("congratulations you won!")


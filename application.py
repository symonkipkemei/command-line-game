
import random


habitat = {1:"front_door",2:"right_door",3:"left_door",4:"central_door",5:"exit_door"}
arsenal = {"sword":0, "key" : 0, "gun":0, "banana":0}


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

    def __init__(self,name,inventory) -> None:
        self.name = name
        self.arsenal = arsenal

    def collect(self, item):
        if item in self.inventory.keys():
            self.inventory[item] += 1

    def attack(self, other):
        choice = random.choice([self.name, other.name])

        if choice  == self.name:
            print(f"{self.name} won!")
        else:
            print(f"{other.name} won!")


class Habitat:
    "maps the environment of the play"

    def __init__(self,name,opponent:bool,collection:bool) -> None:
        self.name = name
        self.opponent = opponent
        self.collection = collection

    def interact(self):
        print("\nOptions:\n**************\n(1).Interact further\n(2).Run to the previous room\n**************")
        self.interact_option = int(input("Your choice: "))

    def fight(self,opponent,hero):
        if self.opponent:
            print(f"\nOptions:\n**************\n(1).fight {opponent.name}\n(2).Run to the previous room\n**************")
            self.fight_option = int(input("Your choice: "))
            if self.fight_option == 1:
                hero.attack(opponent)
    def __str__(self) -> str:
        return f"Welcome to the land of milk and war \nAt {self.name} we love vistors. Battles happen and sometime warriors die "
        
        

front_door = Habitat("front",opponent=True,collection=True)
black_panther = Opponent("Black panther","On land",5)
warrior = Hero("symon",inventory=arsenal)


print(front_door)
front_door.fight(black_panther,warrior)
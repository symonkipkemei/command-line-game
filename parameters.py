import time
import random
import requests



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

    def __init__(self,name) -> None:
        self.name = name
        self.arsenal = {"sword":0, "key" : 0, "gun":0, "banana":0}

    def collect(self, item):
        print(f"\nYou have found a {item}!")
        print("****************")
        print("(1).Take it\n(2).Leave it")
        print("****************")
        user_option = int(input("Your choice: "))
        if user_option == 1:
                self.arsenal[item] += 1
    def decollect(self):
        for key,pair in self.arsenal.items():
            self.arsenal[key] = 0

    def attack(self, other):

        #if the hero wins he has an option of collecting  inventory item

        options = [self.name, other.name]
        choice = random.choice(options) 
        # emojis to display a fight
      
        if choice  == self.name:
            print(f"Congratulations {self.name},  won!")
            collect = True
        else:
            print(f"{other.name} defeated you!")
            print("🤕🤕🥵🤕🤕🤕")
            collect = False
        return collect


#options that control the gameplay in Habita blueprint
options = ["Fight","Collect","empty"]

class Habitat:
    "maps the environment of the play depending on the options"

    def __init__(self,name,option) -> None:
        self.name = name
        self.option = option

    def interact_with(self, Opponent,Hero):
                    # allow user to select option between fighting an opponent, collecting , empty room , entering a locked room
        # fighting
        if self.option == options[0]:
            print(f"You've found {Opponent.name} !")
            print(f"\nOptions:\n**************\n(1).{options[0]} {Opponent.name}\n(2).Run to the previous room\n**************")
            self.fight_option = int(input("Your choice: "))
            if self.fight_option == 1:
                hero_win = Hero.attack(Opponent)
                if not hero_win:
                    Hero.decollect()
            elif self.fight_option == 2:
                exit = True
            else:
                print("wrong input")

        #collecting
        elif self.option == options[1]:
            # abstract collection from Hero's possible arsenals into a list
            collections = [arsenal for arsenal in Hero.arsenal.keys()]
            choice = random.choice(collections)

            print(f"You've found {choice} !")
            Hero.collect(choice)
            

        #empty room
        elif self.option == options[2]:
            print("You've entered an empty room")
            
            print(f"\nOptions:\n**************\n(1).Run to the previous room\n**************")
            self.further_option = int(input("Your choice: "))
            if self.further_option == 1:
                exit = True
            else:
                print("wrong input")
    

    def __str__(self) -> str:
        return f"Welcome to the land of milk and war \nAt {self.name} we love vistors. Battles happen and sometime warriors die "

# display door options available
def door_choices(*args) -> int:
    """Allows the player to make a choice between the available doors:
    Returns:
        int: the key pair of the chosen door
    """
    #easily retrieve door names using dictionaries keys
    opt ={}
    print("\nThere are five doors")
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

# welcoming the user
def player_name() -> str:
    """Collect user_name and welcome him/her to the game

    Returns:
        str: player name
    """

    # The name of the player
    player = input("What's your name ? : ")
    player = str.capitalize(player)

    # give the player a new name from API


    
  
    #The welcome message
    print("________________________________")
    print("(◕‿◕)THE CAVES OF KAPKOLE(◕‿◕)")
    print("________________________________")
    print(f"""Hello {player},
The princess of Kapkole Kingdom is stuck in
the caves with dungeons and dragons (~_~).
Fortunately, she is still alive.
You've been entrusted to find and 
bring her home.
________________________________
      """)


    time.sleep(5)


    print("\n________________________________")
    print("""All the best in your search.
________________________________
 """)
    
    time.sleep(2)

    return player


def main():
    """The game is about finding a lost princess within the dungeons of the dragons. The princess is locked in one of the rooms! Will you be the hero! 
    or will you be part of the statistics of the fallen soldiers!
    """

    # creating objects
    #__________________________________________________________________
    #Hero
    warrior = Hero("symon")

    #habitats
    # each environment is characterised by different options (fight, collect or an empty room)
    front_door = Habitat("Namibia",option=options[0])
    right_door = Habitat("Bostwana",option=options[1])
    left_door = Habitat("Malawi",option=options[2])
    back_door = Habitat("Kenya",option=options[0])
    exit_door = Habitat("Exit",option=options[0])

    #opponents
    black_panther = Opponent("Black panther","On land",5)
    gorilla =Opponent("gorilla","forest",4)
    prey_mantis =Opponent("Prey Mantis","trees",3)

    #__________________________________________________________________


    # welcome the user to the game
    player_name()

  
    play_again = True
    while play_again:
        # state the state of the inventory
        print(warrior.arsenal)
        # Game begins, no way out unless you rescue the girl or you are defeated
        return_previous_room = True
        while return_previous_room:
            # display the door choices
            selection = door_choices(front_door.name,right_door.name,left_door.name,back_door.name,exit_door.name)
            if selection == front_door.name:
                front_door.interact_with(black_panther,warrior)

            elif selection == right_door.name:
                right_door.interact_with(gorilla,warrior)

            elif selection == left_door.name:
                left_door.interact_with(prey_mantis,warrior)

            elif selection == back_door.name:
                back_door.interact_with(prey_mantis,warrior)

            elif selection == exit_door.name:
                print("\n“There is no failure except in no longer trying.”― Elbert Hubbard.")
                return_previous_room = False

            else:
                print("Wrong input, try again\n")
            
            print()
            print(warrior.arsenal)

        user_choice = input("\nDo you want to play again? (y/n):")
        user_choice =str.lower(user_choice)
        if user_choice == "y":
            play_again = True
        elif user_choice == "n":
            print("""\n“Maybe there are times when one should welcome defeat, tell it to come right in and sit down.”
― Iris Murdoch,""")
            play_again = False


if __name__ == "__main__":
    main()
    

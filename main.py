
from parameters import *


def main():
    """The game is about finding a lost princess within the dungeons of the dragons. The princess is locked in one of the rooms! Will you be the hero! 
    or will you be part of the statistics of the fallen soldiers!
    """

    # welcome the user to the game
    player = player_name()

    # creating objects
    #__________________________________________________________________
    #Hero
    warrior = Hero(player)
    
    #opponents
    black_panther = Opponent("Black panther","On land",5)
    gorilla =Opponent("gorilla","forest",4)
    prey_mantis =Opponent("Prey Mantis","trees",3)
    baboon =Opponent("Baboon","trees",2)
    cheetah =Opponent("Baboon","trees",2)
    #__________________________________________________________________

    play_again = True
    while play_again:
        # state the state of the inventory
        print(warrior.arsenal)
        # Game begins, no way out unless you rescue the girl or you are defeated
        return_previous_room = True
        while return_previous_room:
            doors = {1:"front_door", 2:"back_door", 3:"central_door", 4:"exit_door"}
            # display the door choices
            selection = door_choices(doors)
            if selection == doors[1]:
                # fight if he wins collect allow the player to collect an item, if he loses all items are retrieved
                win = warrior.attack(black_panther)
                if win:
                    warrior.collect()
                else:
                    warrior.decollect()

            if selection == doors[2]:
                # enters a room collect item
                warrior.collect()

            elif selection == doors[3]:
                #door locked needs a key to open
                if warrior.arsenal["key"] > 1:
                    print("You have found the daughter of the king . congratulations!")
                    return_previous_room = False
                else:
                    print("The door is locked, you need to find a key")

            elif selection == doors[4]:
                #exit the game
                print("\n“There is no failure except in no longer trying.”― Elbert Hubbard.")
                return_previous_room = False
            print(warrior.arsenal)
        #play again option
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
    



from parameters import *

def main():
    """The game is about finding a lost princess within the dungeons of the dragons. The princess is locked in one of the rooms! Will you be the hero! 
    or will you be part of the statistics of the fallen soldiers!
    """

    # creating objects
    #__________________________________________________________________
    #Hero
    warrior = Hero("symon")

    

    #habitats

    #options that control the gameplay in Habitat blueprint
    options = ["Fight","Collect","empty"]
        
    # each environment is characterised by different options (fight, collect or an empty room)
    front_door = Habitat("Namibia",option=options[0])
    right_door = Habitat("Bostwana",option=options[1])
    left_door = Habitat("Malawi",option=options[2])
    back_door = Habitat("Kenya",option=options[1])
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
                left_door.interact_with(prey_mantis,warrior)

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
    




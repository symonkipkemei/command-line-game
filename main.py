
from sub_programs import *


def main():
    # before the start of the game ,the sword is 0
    sword = 0
    # introduction
    user = player_name()
    user_name = str.capitalize(user)

    # game begins
    return_previous_room = True
    while return_previous_room:
        door_choice = door_choices()
        if door_choice == 1:
            left_door()
            user_option = option()
            if user_option == 1:
                further_option = option_further_left()
                if further_option == 1:
                    sword = sword_found()
                elif further_option == 2:
                    return_previous_room = True
                
        elif door_choice == 2:
            right_door()
            user_option = option()
            if user_option == 1:
                further_option = option_further_right()
                if further_option == 1:
                    if sword == 1:
                        print(f"\nYou were born to win {user_name}, but to be a winner you must plan to win, prepare to win, and expect to win.\ncongratulations!")
                    
                    elif sword == 0:
                        print(f"\nSometimes by losing a battle,you find a new way to win the war.\nRest in peace {user_name}. ")
                    return_previous_room = False

                elif further_option == 2:
                    return_previous_room = True
        else:
            print("Try again")

    

main()
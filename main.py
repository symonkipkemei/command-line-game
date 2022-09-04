
from sub_programs import *


def gameplay_left_door()-> bool:
    """Activities that take place in the left door
    Returns:
        bool: Return to the previous room (central pavillion), if not the game ends
    """
    return_previous_room = True
    left_door()
    user_option = option()
    if user_option == 1:
        further_option = option_further_left()
        if further_option == 1:
            sword = sword_found()
        elif further_option == 2:
            pass
    return return_previous_room

def gameplay_right_door(user_name:str)-> bool:
    """Activities that take place in the right door

    Args:
        user_name (str): The name of the game user

    Returns:
        bool: Return to the previous room (central pavillion), if not the game ends
    """
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

def main():
    # before the start of the game ,the sword is 0
    sword = 0
    # introduction
    name = player_name()

    # game begins
    return_previous_room = True
    while return_previous_room:
        door_choice = door_choices()
        if door_choice == 1:
            return_previous_room = gameplay_left_door()
        elif door_choice == 2:
            return_previous_room = gameplay_right_door(name)
        else:
            print("Try again")

    

main()
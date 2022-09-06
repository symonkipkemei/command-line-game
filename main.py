
from parameters import *


def gameplay_left_door(filepath, user_name = "player")-> bool:
    """Game play : The left room is empty, but if you look around you will find a sword.

    Args:
        user_name (str): The name of the player

    Returns:
        bool: Return to the previous room (central pavillion), if not the game ends
    """
    return_previous_room = True
    # what's in the room
    what_is_in_the_room(f"Oops {user_name}! You entred an empty room")
    user_option = option_to_interact()
    if user_option == 1:
        further_option = option_further("Look around")
        item_name = "sword"
        if further_option == 1:
            sword_no = item_found(item_name)
            record_inventory(filepath, item_name, sword_no)
        elif further_option == 2:
            pass
    return return_previous_room

def gameplay_right_door(filepath, user_name = "player")-> bool:
    """There is a dragon in the right room, you have to fight it. To fight it you need at least one sword.If you win, there are items that you can collect.

    Args:
        user_name (str): The name of the player

    Returns:
        bool: Return to the previous room (central pavillion), if not the game ends
    """

    print("\nFireeeee! I am the dragon, I am going to eat you alive !!")

    user_option = option_to_interact()

    if user_option == 1:
        further_option = option_further("fight")
        if further_option == 1:
            #check if the user has a sword
            record = retrieve_inventory(filepath)
            for key, value in record.items():
                if key == "sword" and int(value) > 0:
                    print(f"\nYou were born to win {user_name}\ncongratulations the dragon is dead!")
                    # interact_further
                    option = option_further("Look beside the dragon", "Look behind the dragon")
                    if option == 1:
                        item = "mangoes"
                         # There is a gun and a sword
                        item_no = item_found(item)
                        record_inventory(filepath, item,item_no)
                    elif option == 2:
                         # There is a gun and a sword
                        item = "gun"
                        item_no = item_found(item)
                        record_inventory(filepath, item, item_no)
                else:
                    print("Rest in peace , we live to fight another day")

        elif further_option == 2:
            return_previous_room = True

def gameplay_back_door(filepath, user_name = "player")-> bool:
    """Game play :There is a chimpanzee with a key, to get the key, you must feed it or kill it

    Args:
        user_name (str): The name of the player

    Returns:
        bool: Return to the previous room (central pavillion), if not the game ends
    """
    print("\n Auu! Auu!, I am a chimpanzee, this is my territory!! , what do you want?")
    
    user_option = option()
    if user_option == 1:
        record = retrieve_inventory(filepath)
        further_option = option_further("Fight the baboon", "Feed the baboon")
        if further_option == 1:
            # Gun needed to fight 
            for key, value in record.items():
                if key == "gun" and int(value) > 0:
                    print(f"\nYou were born to win {user_name}\ncongratulations the the baboon is dead!")
                    # interact_further
                    option = option_further("Look beside the baboon")
                    if option == 1:
                       item_collected = "key"
                       item_no = item_found(item_collected)
                       record_inventory(filepath, item_collected, item_no)

def gameplay_front_door(filepath, user_name = "player")-> bool:
    """Game play: There is a princess , locked in this room. You need a key to rescue her.

    Args:
        user_name (_type_): The name of the player

    Returns:
        bool: Return to the previous room (central pavillion), if not the game ends
    """

    record = retrieve_inventory(filepath)

    for key, value in record.items():
        if key == "key" and int(value) > 0:
            print(f"Congratulations {user_name}, you've just rescued the king's daughter!")
            return False
        else:
            print(f"\n Ooops!,{user_name} The door appears to be closed, you need to find the key")

    
def main():
    """The game is about finding a lost princess within the dungeons of the dragons. The princess is locked in one of the rooms! Will you be the hero! 
    or will you be part of the statistics of the fallen soldiers!
    """

    # reset the inventory
    filepath = "user_items.csv"
    clean_inventory(filepath)

    # introduction
    name = "symon"

    # Game begins, no way out unless you rescue the girl or you are defeated
    return_previous_room = True
    while return_previous_room:
        door_choice = door_choices()
        if door_choice == 1:
            return_previous_room = gameplay_left_door(filepath,name)
        elif door_choice == 2:
            return_previous_room = gameplay_right_door(filepath,name)
        elif door_choice == 3:
            return_previous_room = gameplay_front_door(filepath,name)
        elif door_choice == 4:
            return_previous_room = gameplay_back_door(filepath,name)
        else:
            print("Wrong input, try again")

    


main()



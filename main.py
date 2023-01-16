import csv
import random
from parameters import *

arsenal_no = 1
multiplier = random.randrange(1,2)
arsenal_no = arsenal_no  * multiplier


def gameplay_left_door(filepath, user_name = "player")-> bool:
    """Game play : The left room is empty, but if you look around you will find a sword.

    Args:
        user_name (str): The name of the player

    Returns:
        bool: Return to the previous room (central pavillion), if not the game ends
    """
    return_previous_room = True
    # what's in the room
    what_is_in_the_room(f"Oops {user_name}! You entered an empty room")
    user_option = option_to_interact()
    if user_option == 1:
        further_option = option_further("Look around")
        item_name = "sword"
        if further_option == 1:
            item_found(item_name,filepath)
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
    print("Tip**You need a weapon in your arsenal to fight the dragon**")
    return_previous_room = True
    user_option = option_to_interact()
    if user_option == 1:
        further_option = option_further("Fight")
        if further_option == 1:
            #check if the user has a sword
            record = retrieve_inventory(filepath)
            total_count = total_item_options(record)
            
            count = 0
            for key, value in record.items():
                if key == "sword" and int(value) >= arsenal_no:
                    print(f"\nThe dragon is dead! Congratulations {user_name}")
                    print("All the best in your search for the princess!")
                    # interact_further
                    option = option_further("Look beside the dragon", "Look behind the dragon")
                    if option == 1:
                        item_found("banana",filepath)
                        return_previous_room = True
                    elif option == 2:
                         # There is a gun and a sword
                        item_found("gun",filepath)
                        return_previous_room = True
                        
                else:
                    count += 1
            if count >= total_count:
                print(f"\nIt was daring of you to fight with your bear hands.\nRest in Peace {user_name}.\n")
                return_previous_room = False

                
        elif further_option == 2:
            return_previous_room = True


    elif user_option == 2:
        return_previous_room = True

    return return_previous_room


def gameplay_back_door(filepath, user_name = "player")-> bool:
    """Game play :There is a chimpanzee with a key, to get the key, you must feed it or kill it

    Args:
        user_name (str): The name of the player

    Returns:
        bool: Return to the previous room (central pavillion), if not the game ends
    """
    print("Auu! Auu!, I am a baboon, this is my territory!, what do you want?")
    print("Tip**You need a weapon in your arsenal to fight the baboon or food to feed it.**")
    count = 0
    user_option = option_to_interact()
    return_previous_room = True
    if user_option == 1:
        record = retrieve_inventory(filepath)
        total_count = total_item_options(record)
        further_option = option_further("Fight the baboon", "Feed the baboon")
        if further_option == 1:
            # Gun needed to fight 
            for key, value in record.items():
                if key == "gun" and int(value) == arsenal_no:
                    print(f"\n Congratulations the the baboon is dead!")
                    print("All the best in your search for the princess!")
                    # interact_further
                    option = option_further("Look beside the baboon")
                    if option == 1:
                       item_found("key",filepath)
                       return_previous_room = True
                    elif option == 2:
                        return_previous_room = True
                else:
                    count += 1
            if count >= total_count:
                print(f"\nWinning isn’t everything, it’s the only thing.\nRest in Peace {user_name}\n The baboon beat you thoroughly\n")
                return_previous_room = False

        elif further_option == 2:
            #feed the baboon
            for key, value in record.items():
                if key == "banana" and int(value) >= arsenal_no:
                    print(f"\nCongratulations the the baboon is satiated and sleepy!")
                    print("All the best in your search for the princess!")
                    #interact further
                    option = option_further("Look beside the baboon")
                    if option == 1:
                       item_found("key",filepath)
                       return_previous_room = True
                    elif option ==2:
                        return_previous_room = True
                else:
                    count += 1
            #To prevent typing several times
            if count >= total_count:
                print(f"\nWinning isn\’t everything, it’s the only thing.\nRest in Peace {user_name}\nThe baboon beat you thoroughly.\nNext time carry food for the baboon.")
                return_previous_room = False

        elif further_option == 3:
            return_previous_room =True
    elif user_option == 2:
        return_previous_room =True

    return return_previous_room
    
    
def gameplay_front_door(filepath, user_name = "player")-> bool:
    """Game play: There is a princess , locked in this room. You need a key to rescue her.

    Args:
        user_name (_type_): The name of the player

    Returns:
        bool: Return to the previous room (central pavillion), if not the game ends
    """
    record = retrieve_inventory(filepath)
    total_count = total_item_options(record)

    # count
    count = 0
    for key, value in record.items():
        if key == "key" and int(value) >= arsenal_no:
            print(f"Congratulations {user_name}, you've just rescued the king's daughter!")
            return False
        else:
            count += 1
            
    if count >= total_count:
        print(f"Ooops {user_name}!\nThe front door is closed,you need to find the key\nAll the best in your search for the princess!")
        return_previous_room = True

    return return_previous_room
    

    
def main():
    """The game is about finding a lost princess within the dungeons of the dragons. The princess is locked in one of the rooms! Will you be the hero! 
    or will you be part of the statistics of the fallen soldiers!
    """


    # play-again
    # reset the inventory
    filepath = "user_items.csv"
    clean_inventory(filepath, "sword","key","gun","banana")

    # introduction
    name = player_name()
        
    play_again = True
    while play_again:
        # state the state of the inventory
        read_inventory()
        # Game begins, no way out unless you rescue the girl or you are defeated
        return_previous_room = True
        while return_previous_room:
            door_choice = door_choices()
            if door_choice == 1:
                return_previous_room = gameplay_front_door(filepath,name)
                read_inventory()
            elif door_choice == 2:
                return_previous_room = gameplay_right_door(filepath,name)
                read_inventory()
            elif door_choice == 3:
                return_previous_room = gameplay_left_door(filepath,name)
                read_inventory()
            elif door_choice == 4:
                return_previous_room = gameplay_back_door(filepath,name)
                read_inventory()
            elif door_choice == 5:
                print("\n“There is no failure except in no longer trying.”― Elbert Hubbard.")
                return_previous_room = False
            elif door_choice == 6:
                print("Insert a digit, try again: ")
            else:
                print("Wrong input, try again\n")

        user_choice = input("\nDo you want to play again? (y/n):")
        user_choice =str.lower(user_choice)
        if user_choice == "y":
            # clean the inventory if the user is to play again
            clean_inventory(filepath, "sword","key","gun","banana")
            play_again = True
        elif user_choice == "n":
            print("""\n“Maybe there are times when one should welcome defeat, tell it to come right in and sit down.”
― Iris Murdoch,""")
            play_again = False


if __name__ == "__main__":
    main()
    




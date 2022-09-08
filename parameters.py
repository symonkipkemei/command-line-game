   
"""Parameters/Logic for the game,the thinniest/repetitive ideas are organised in this directory"""

import time
import csv

#Common parameters: applies to the game
def what_is_in_the_room(message:str):
    """Display what is in the room

    Args:
        message (str): Message to the player
    """
    print(message)

def player_name() -> str:
    """Collect user_name and welcome him/her to the game

    Returns:
        str: player name
    """

    # The name of the player
    player = input("What's your name ? : ")
    player = str.capitalize(player)
  
    #The welcome message
    print("________________________________")
    print("(◕‿◕)THE CAVES OF KAPKOLE(◕‿◕)")
    print("________________________________")
    print(f"""Hello {player},
The king of Kapkole Kingdom has lost her daughter 
in the caves with dungeons and dragons (~_~).
Fortunately, she is still alive.
Your instinctual responsibility as a warrior is to save her.
________________________________
      """)


    time.sleep(10)


    print("\n________________________________")
    print("""There are four dungeons, with four doors.
Your mission is to rescue the princess
You are allowed to scream,
You are allowed to cry,
But there is no way back.
________________________________
 """)
    
    time.sleep(10)

    return player

def door_choices() -> int:
    """Allows the player to make a choice between the available doors, The doors are : 
    1. left
    2. right
    3. front
    4. back

    Returns:
        int: the key pair of the chosen door
    """
    print("\nThere are four doors\n*********************\n(1).Left door\n(2).Right door\n(3).Front door\n(4).Back door\n*********************")
    door_choice = int(input("Make your choice:"))
    print("\n")


    return door_choice

# data storage,retrieving and cleaning
def record_inventory(file_path, item: str,item_no: int):
    """Records the collected item and the item number into a persistent memory(csv).

    Args:
        item (str): The name of the collected item;
        item_no(int): The number of items collected

    Returns:
        None: None
    """
    #retrieve information from stored media
    inventory = {}
    with open(file_path, "r") as f:
        read_obj = csv.reader(f)
        dd_list = list(read_obj)
        
        for x in dd_list:
            inventory[x[0]] = x[1]

    # change the inventory based on the item added
    for key,value in inventory.items():
        if key == item:
            inventory[key] = int(value) + item_no
        
    #save the changes back to the csv file
    with open(file_path, "w") as f:
        obj = csv.writer(f)
        dd_list = []
        for key, value in inventory.items():
            data = [key, value]
            dd_list.append(data)
        
        obj.writerows(dd_list)
            
def retrieve_inventory(file_path) -> dict:
    """Opens a csv file, reads information and abstract data to a dictionary

    Args:
        file_path (csv): Opens a csv file

    Returns:
        dict: dictionary containing all the game inventory items
    """
    inventory = {}

    with open(file_path, "r") as f:
        obj_reader = csv.reader(f)
        dd_list = obj_reader
        for item in dd_list:
            inventory[item[0]] = item[1]
    
    return inventory

def clean_inventory(file_path, *args: str):
    """Clean the inventory before the game starts

    Args:
        file_path (csv): The path for the file storage
        args (str): Items to be included in the inventory
    """
    #append items to a dictionary
    inventory = {}

    for item in args:
        inventory[item] = 0


    with open(file_path, "w") as f:
        obj = csv.writer(f)
        dd_list = []
        for key, value in inventory.items():
            data = [key, value]
            dd_list.append(data)
        
        obj.writerows(dd_list)

# options when playing the game, applies to all rooms

def option_to_interact() -> int:
    """After entering the right,left,front or back door. The player has two options:
     1. Interact further
     2. Run to the previous room

    Returns:
        int: The key pair of the choice made by the player.
    """
    
    print("\nOptions:\n**************\n(1).Interact further\n(2).Run to the previous room\n**************")
    option_user = int(input("Your choice: "))

    return option_user

def item_found(item:str) -> int:
    """After Looking around, the player spots an item, he/she has an option to take it or leave it. The item can be:
    1. sword
    2. key
    3. gun
    4. mangoes

    Args:
        item (str): The name of the item

    Returns:
        int: The number of items picked by the player
    """
    item_no = 0
    try_again = True
    while try_again:
        print(f"\nYou have found a {str.capitalize(item)}!")
        print("****************")
        print("(1).Take it\n(2).Leave it")
        print("****************")
        user_option = int(input("Your choice: "))
        if user_option == 1:
            item_no += 1
            print(f"\nYou now have a {item} in your collection!\nAll the best in your search for the princess!")
            try_again = False
        elif user_option == 2:
            item_no += 0
            try_again = False
        else:
             print("Wrong input, try again")
    return item_no
    
def option_further(*args:str)-> int:
    """Organise the arguments obtained into index, option and display to the player:
    1. option 1: what happens?
    2. option 2: what happens?
    3. option 3: ..........(continues)
    4. run to previous room (default)

    Args:
        args (str): Options for the gameplay

    Returns:
        int: The key pair of the choice made by the user.
        None: when the player selects:run to the previous room.
    """
    # organise the parameters obtained, organise into index,item and 
    options_dict = {}
    default_option = "Run to the previous room"
    for index, option in enumerate(args,1):
        options_dict[index] = option

    last_item = index + 1
    options_dict[last_item] = default_option

    try_again = True
    while try_again:
        # display to the user
        print("\nOptions: ")
        print("****************")
        for key, value in options_dict.items():
            print(f"({key}). {value}")
        print("****************")
        user_option = input("Your choice: ")

        if user_option.isdigit():
            user_option = int(user_option)
            if user_option in options_dict.keys():
                if user_option == last_item:
                    try_again = False
                    pass
    
                else:
                    try_again = False
                    return user_option
            else:
                print("The option is not available, try again")
        else:
            print("Please insert a digit, try again: ")
    




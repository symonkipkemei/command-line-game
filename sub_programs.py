import time


def player_name() -> str:
    """Collect user_name and welcome him/her to the game

    Returns:
        str: player name
    """

    # The name of the player
    player = str.capitalize(input("What's your name ? : "))
  
    #The welcome message

    print(f"\nWelcome {player} to the:")
    print(
        '''
  ______   ______   .___  ___. .___  ___.      ___      .__   __.  _______  
 /      | /  __  \  |   \/   | |   \/   |     /   \     |  \ |  | |       \ 
|  ,----'|  |  |  | |  \  /  | |  \  /  |    /  ^  \    |   \|  | |  .--.  |
|  |     |  |  |  | |  |\/|  | |  |\/|  |   /  /_\  \   |  . `  | |  |  |  |
|  `----.|  `--'  | |  |  |  | |  |  |  |  /  _____  \  |  |\   | |  '--'  |
 \______| \______/  |__|  |__| |__|  |__| /__/     \__\ |__| \__| |_______/ 
                                                        
        
        ''', end=" "
    )

    time.sleep(3)

    print(
        '''
 __       __  .__   __.  _______ 
|  |     |  | |  \ |  | |   ____|
|  |     |  | |   \|  | |  |__   
|  |     |  | |  . `  | |   __|  
|  `----.|  | |  |\   | |  |____ 
|_______||__| |__| \__| |_______|
                                  
        ''', end=" "
    )

    time.sleep(3)

    print(
        '''
  _______      ___      .___  ___.  _______ 
 /  _____|    /   \     |   \/   | |   ____|
|  |  __     /  ^  \    |  \  /  | |  |__   
|  | |_ |   /  /_\  \   |  |\/|  | |   __|  
|  |__| |  /  _____  \  |  |  |  | |  |____ 
 \______| /__/     \__\ |__|  |__| |_______|
                                            
        '''
    )

    print("There is no way back, You either win! or you die !\n")

    return player


def door_choices() -> int:
    """Allows the player to make a choice between the available doors

    Returns:
        int: the key pair of the chosen door
    """
    print("\nThere are two doors\n(1).Left door\n(2).Right door")
    door_choice = int(input("Make your choice: "))

    return door_choice

def left_door():
    """Game play at the left door
    """
    print("Oops! You've entered an empty room")

def right_door():
    """Gameplay at the right door
    """
    print("\nFireeeee! I am the dragon, I am going to eat you alive !!")
    

def option() -> int:
    """After entering the right/left door. The player has an option of interacting further or returning to previous room

    Returns:
        int: The key pair of the choice made by the player.
    """
    
    print("\nYou have two options\n(1).Interact further\n(2).Run to the previous room")
    user_option = int(input("Make your choice: "))

    return user_option

def option_further_right() -> int:
    """After selecting interacting further, the player has two options in the right room,fight or escape the room

    Returns:
        int: The key pair of the choice made by the player
    """
    
    print("\nYou have two options\n(1).fight\n(2).Run to the previous room")
    user_option = int(input("Make your choice: "))
    return user_option

def option_further_left() -> int:
    """After selecting Interacting further the user has two options, look around or run to previous room

    Returns:
        int: The key pair of the choice made by the player
    """
    print("\nYou have two options\n(1).Look around\n(2). Run to the previous room")
    user_option = int(input("Make your choice: "))
    if user_option == 1:
        return user_option
    elif user_option == 2:
        return user_option


#if the user happens to find the sword, assign variable to one
sword = 0

def sword_found() -> int:
    """After looking around in the left room, the player spots a sword. He has an option to take it or leave it.
    When the player comes back to this room he can take another sword.

    Returns:
        int: The number of swords in possesion with the player,the default number is 0
    """
    
    global sword
    print("\nYou have found a sword!\n(1).Take it\n(2).Leave it")
    user_option = int(input("Make your choice: "))
    if user_option == 1:
        sword += 1
        if sword == 1:
            print("\nYou have sword now, may you win the battle.")
        elif sword >= 2:
            print("\nYou already have a sword in your hand, one sword is enough to win the battle.\nGood luck!")
            sword = 1
    elif user_option == 2:
        sword = 0
    return sword

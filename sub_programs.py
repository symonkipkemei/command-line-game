import time
#if the user happens to find the sword, assign variable to one
sword = None

def player_name():
    """Collect user_name and welcome him/her to the game"""
    player = input("What's your name ? : ")

    print(f"\nWelcome {player_name} to the:")
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


def door_choices():
    print("There are two doors\n(1).Left door\n(2).Right door")
    door_choice = int(input("Make your choice: "))

    return door_choice

def left_door():
    print("Oops! You've entered an empty room")

def right_door():
    print("\nFireeeee! I am the dragon, I am going to eat you alive !!")
    

def option():
    """You have an option of interacting further or return to previous room"""
    print("\nYou have two options\n(1).Interact further\n(2).Run to the previous room")
    user_option = int(input("Make your choice: "))

    return user_option

def option_further_right():
    print("\nYou have two options\n(1).fight\n(2).Run to the previous room")
    user_option = int(input("Make your choice: "))
    return user_option

def option_further_left():
    """Option further"""
    print("\nYou have two options\n(1).Look around\n(2). Run to the previous room")
    user_option = int(input("Make your choice: "))
    if user_option == 1:
        return user_option
    elif user_option == 2:
        return

def sword_found():
    """Sword found"""
    print("\nYou have found a sword!\n(1).Take it\n(2). Leave it")
    user_option = int(input("Make your choice: "))
    if user_option == 1:
        sword = 1
        return sword
    elif user_option == 2:
        sword = 0
        return sword

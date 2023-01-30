


import time

def door_choices() -> int:
    """Allows the player to make a choice between the available doors, The doors are : 
    1. front
    2. right
    3. left
    4. back
    5. exit

    Returns:
        int: the key pair of the chosen door
    """
    print("\nThere are five doors\n_____________________\n(1).Front door\n(2).Right door\n(3).Left door\n(4).Back door\n(5).Exit door\n_____________________")
    door_choice = input("Make your choice:")
    print("\n")
    if door_choice.isdigit():
            door_choice = int(door_choice)
    else:
        door_choice = 6
    return door_choice



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
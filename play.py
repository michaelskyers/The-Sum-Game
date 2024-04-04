from random import randint
from random import choice
import time

def valid_input(message,floor,ceiling):
    while True:
        number = input(message)

        if number.isdigit() and int(number) >= floor and int(number) <= ceiling:
            return number
        else:
            print("Invalid input: either not a number or outside of range\n")

def welcome(target = 25, choices = 3):
    print(""
      +"\nWelcome to the sum game".upper()
      +f"\nObjective: Force opponent to get a sum of {target} or more"
      +"\n\nHow to play:"
      +f"\n\t1. Two players take turns choosing a number between and {choices} (inclusive), then add it to a running total."
      +f"\n\t2. First person to get the total to {target} or more loses."
      +"\n\nThe target and choice range can be changed in the settings menu.")

    input("\nPress ENTER when you are ready to play...")

def main_menu(target = 25, choices = 3, player = 1):
    print(""+
          "\n##########################"+
          "\nCurrent Settings"+
          "\n##########################"+
          f"\nChoice Range: 1 to {choices}"+
          f"\nTarget Total: {target}")

    print(""+
          "\n>>>>>>>>Game Menu<<<<<<<<<"+
          "\n1. Player vs Player"+
          "\n2. Player vs AI"+
          "\n3. Game Settings"+
          "\n4. Exit")
    user_choice = valid_input("\nPlease select an option by entering the number: ",1,4)
    option = int(user_choice)

    match(option):
        case 1:
            gameloop(target, choices, player)
        case 2:
            ai_gameloop(target, choices)
        case 3:
            game_settings(target, choices)
        case 4:
            print("Thank you for playing!")

def gameloop(target, choices, player):
    """
    Gameloop for two human players
    """
    total = 0
    while (total < target):
        print("\nPlayer",player)
        number = valid_input(f"How much would you like to add to the total? (Number between 1 and {choices} (inclusive)\n> ",1,choices)
        total += int(number)
        opponent = abs(3 - player)

        print("TOTAL:",total)

        if total >= target:
            print(f"\nSorry, you lost. Player {opponent} wins!")

        player = opponent

    play_again = valid_input("\nWould you like to play again?"+
                             "\n1. Yes, let's go!"+
                             "\n2. Return to main menu\n> ",1,2) == "1"

    if play_again:
        gameloop(target, choices, 1)
    else:
        main_menu(target, choices, player)

def ai_gameloop(target, choices):
    """
    Defines behaviour for AI opponent based on selected difficulty
    """

    def ai_choice(wait_time, difficulty, total, choices):

        time.sleep(wait_time)
        choices_plus_one = choices + 1
        
        if difficulty == 2:
            if total % choices_plus_one == 0:
                return randint(1,choices)
            else:
                return choices_plus_one - (total % choices_plus_one)

        return randint(1,choices)
    
    difficulty = int(valid_input(
    """
    Select difficult by entering a number:
    1. AI Padawan
    2. AI Master
    > """,1,2))

    player = randint(1,2)
    opponent = abs(3 - player)
    player_turn = True if player == 1 else False

    human = f"Player {player}: Humanity"
    ai = f"Player {opponent}: AI"

    total = 0
    wait = 2 if difficulty == 2 else 0

    # power ups
    power_ups = {
        "Time Warp": "Player is able to skip current turn",
        "Double Strike": "Player is able to play twice in a given turn",
        "Surge Overflow": "Player is able to add one more than the choice limit",
        "Depletion Burst": "Player is able to subtract one more than the choice limit"
        }

    def activate_ability(ability, choices, is_ai, total):
        
        match (ability):
            case "Time Warp":
                if is_ai:
                    print("The AI has skipped its turn.")
                else:
                    print("You have skipped your turn.")
                
                time.sleep(2)
                return 0
            
            case "Double Strike":
                if is_ai:
                    number = ai_choice(0, 2, total, choices)
                    time.sleep(1)
                    print("1st number selected")
                    
                    total += number

                    number += ai_choice(0, 2, total, choices)
                    time.sleep(1)
                    print("2nd number selected")

                    return number
                
                number = int(valid_input("Please select your first number: ",1,choices))
                number += int(valid_input("Please select your second number: ",1,choices))
                return number
            
            case "Surge Overflow":
                print("Amount to be added is", choices + 1)
                return choices + 1
            
            case "Depletion Burst":
                print("Amount to be subtracted is", choices + 1)
                return -(choices + 1)

    player_power = choice(list(power_ups.keys()))
    ai_power = choice(list(power_ups.keys()))

    while total < target:
        print()
        
        if player_turn:
            print(human)
            if player_power != "":
                print(f"Special ability available\n-> {player_power}: {power_ups[player_power]}")

                use_ability = int(valid_input(f"\nHow much would you like to add to the total? (Number between 1 and {choices} (inclusive)"+
                                              "\nEnter 0 if you would like to use your ability"+
                                              "\n> ",0,choices)) == 0

                if use_ability:
                    number = activate_ability(player_power, choices, False, total)
                    player_power = ""
                else:
                    number = use_ability
                
            else:
                print("No ability available")
                number = int(valid_input(f"How much would you like to add to the total? (Number between 1 and {choices} (inclusive)\n> ",1,choices))
            
        else:
            print(ai+"\nThinking...")
            time.sleep(2)

            if ai_power != "":
                if total % (choices + 1) == 0 and total > target // 2:
                    print(f"The AI has used {ai_power}!")
                    number = activate_ability(ai_power, choices, True, total)
                    ai_power = ""
                else:
                    number = ai_choice(wait, difficulty, total, choices)
                    print("The AI has chosen", number)
                    
            else:
                number = ai_choice(wait, difficulty, total, choices)
                print("The AI has chosen", number)
            
        total += number
        print("TOTAL:",total)
        print()

        if total >= target:
            if not player_turn:
                to_string = "Well done! That is a victory for humanity!"
            else:
                to_string = "Unfortunately AI is one step closer to world domination. You lost."

            border = "#" * len(to_string)
            print(border,to_string,border, sep = "\n")
                
        player_turn = not player_turn

    play_again = valid_input("\nWould you like to play again?"+
                             "\n1. Yes, let's go!"+
                             "\n2. Return to main menu\n> ",1,2) == "1"

    if play_again:
        ai_gameloop(target, choices)
    else:
        main_menu(target, choices, 1)
        

def game_settings(target, choices):
    """
    Change target total and number of choices
    """
    
    print(""+
          "\nCurrent Settings"+
          "\n##########################"+
          f"\nChoice Range: 1 to {choices}"+
          f"\nTarget Total: {target}\n")

    update_settings = int(valid_input(
        """
        Would you like to change these settings?
        1. Yes
        2. No
        > """,1,2)) == 1

    if update_settings:
        settings = [
            [2, 16],
            [3, 25],
            [3, 45],
            [5, 31],
            [5, 55],
            [8, 64]
            ]

        print(""+
              "\n\t    Available Settings"+
              "\n\t    ------------------"+
              "\n\t    | Range | Target |"+
              "\n\t    ------------------"
              )
        
        for i in range(len(settings)):
            print(f"\t{i + 1}.  |   {settings[i][0]}   |   {settings[i][1]}   |"+
                  "\n\t    ------------------")

        new_setting = int(valid_input("Select a new setting: ",1,len(settings)))
        new_setting = settings[new_setting - 1]
        choices = new_setting[0]
        target = new_setting[1]

    print("Returning to main menu...")
    time.sleep(2)
    
    main_menu(target, choices, 1)

def play():
    """
    Driver function to run the game
    """
    welcome()
    main_menu()

# Starts the game
play()

# other power_up ideas
# force opponent to randomly pick three, shuffle combinations, skip combinations, reverse, allow to pick power ups, guess what will pick, traps

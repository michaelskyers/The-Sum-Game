
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
          "\nGame Menu"+
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
            game_settings()
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
        main_menu()

def ai_gameloop(target, choices):
    """
    Defines behaviour for AI opponent based on selected difficulty
    """
    # allow user to select difficulty (instead of from settings)
    pass

def game_settings():
    """
    Change target total and number of choices
    """
    # Maybe call main_menu again with new settings
    pass

def play():
    """
    Driver function to run the game
    """
    welcome()
    main_menu()

# Starts the game
play()

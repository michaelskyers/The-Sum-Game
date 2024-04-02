target = 25
choices = 3
total = 0
player = 1

print(""
      +"\nWelcome to the sum game".upper()
      +f"\nObjective: Force opponent to get a sum of {target} or more"
      +"\n\nHow to play:"
      +f"\n\t1. Two players take turns choosing a number between and {choices} (inclusive), then add it to a running total."
      +f"\n\t2. First person to get the total to {target} or more loses.")

input("\nPress ENTER when you are ready to play...")

while (total < target):
    print("\nPlayer",player)
    number = input(f"How much would you like to add to the total? (Number between 1 and {choices} (inclusive)\n> ")
    total += int(number)
    opponent = abs(3 - player)

    print("TOTAL:",total)

    if total >= target:
        print(f"\nSorry, you lost. Player {opponent} wins!")

    player = opponent

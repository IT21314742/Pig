import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the Number of Players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

print(players)

max_score = 50
player_scores = [0 for _ in range(players)]

print(player_scores)

while max(player_scores) < max_score:

    current_score = 0

    should_roll = input("would you like to roll (y)?")
    if should_roll.lower() == "y":
        value = roll()
    else:
        break 


    value = roll()
    if value == 1:
        print("You rolled a 1! Turn done!")
        break

    else:
        current_score += value
        print("You rolled a:", value)

    print("Your score is:")

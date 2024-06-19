import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

value = roll()
print(value)  

while True:
    players = input("Enter the Number of Players (1-4): ")
    if players.isdigit():
        players = int(players)
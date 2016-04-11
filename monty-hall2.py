# monty-hall2

# this simulation is if the player SWITCHES.
# Basically, if the random door selected was the winning door, he would lose.
# If the random door picked was a losing door, he would win.
# Remember, one of the losing doors will be eliminated after.

import random

wins = 0
losses = 0


for _ in range(1000):
    winning_door = random.randint(1, 3)
    player_choice = random.randint != winning_door

    if player_choice == winning_door:
        losses += 1

    else:
        wins += 1


def percentage():
    return 100 * float(wins)/1000
y = percentage()

print(str(wins+losses) + ' games')
print('Wins:', wins)
print('Losses:', losses)
print('Winning Percentage:', y)
print('Good choice in switching!')

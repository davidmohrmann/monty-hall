import random

wins = 0
losses = 0
# doors = [1, 2, 3] for staying don't need the doors.
# If switching will need doors.

# could put the stay in a function

for _ in range(1000):
    winning_door = random.randint(1, 3)
    player_choice = random.randint(1, 3)

    if player_choice == winning_door:
        wins += 1
    else:
        losses += 1


def percentage():
    return 100 * float(wins)/1000
y = percentage()

print(str(wins+losses) + ' games')
print('Wins:', wins)
print('Losses:', losses)
print('Winning Percentage:', y)
print("According to these statistics, you better switch your choice!")

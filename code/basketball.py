# Basketball program

import random

throw_result = ('through hoop', 'miss')


# Function definitions
def shoot_hoops(player_number):
    player_score = 0
    for throw in range(15):
        player_result = random.choice(throw_result)
        if player_result == 'through hoop':
            player_score += 1  # this means player_score = player_score + 1
    print(player_number + " score: " + str(player_score))
    return player_score


def compare_score():
    if player_1_score > player_2_score:
        print("\nPlayer #1 got a higher score!")
    elif player_2_score > player_1_score:
        print("\nPlayer #2 got a higher score!")
    else:
        print("\nIt's a tie!")


# Function calls
player_1_score = shoot_hoops('Player #1')
player_2_score = shoot_hoops('Player #2')
compare_score()

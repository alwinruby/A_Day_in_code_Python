#Miniture Golf Program

from random import randint

#Each value of the dictionary is initialised as an empty list
scores = {'Player #1': [], 'Player #2': [], 'Player #3': [], 'Player #4': []}

#Add 18 randomly chosen numbers to eacy dictionary value (a list)
for hole_number in range(1, 19): # outer for loop
    print("Hole #" + str(hole_number) + " begins")
    for player_number, score_list in scores.items(): # inner for loop
        golf_strokes = randint(1, 7) # get random integer from 1 through 7
        scores[player_number].append(golf_strokes)
        print(player_number + " scored " + str(golf_strokes))
    print("Hole #" + str(hole_number) + " is done.\n")

for player_number, score_list in scores.items():
    scores[player_number] = sum(score_list)
    print(player_number + " final score: " + str(sum(score_list)))

wining_score = min(scores.values())

for player_number, score_list in scores.items():
    if score_list == wining_score:
        print("\n" + player_number + " won!")
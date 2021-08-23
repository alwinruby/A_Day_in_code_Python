# Balloon program

# Function definition
def choose_ballons(*our_choice):
    balloons = [] # create empty list
    for colour_choice in our_choice:
        balloons.append(colour_choice + ' balloon')
        print("I got a " + colour_choice + ' balloon')
    return balloons # return list

def travel(transport, destination = 'our house'):
    print("\nWe are " + transport + " to " + destination + ".")

balloon_colours = ['yellow', 'blue', 'purple', 'green', 'red', 'pink']
del balloon_colours[4] # delete 'red'
for balloon in balloon_colours:
    print("Available balloon colour: " + balloon.title())

first_balloons = choose_ballons('blue', 'purple') # function call
second_balloons = first_balloons[:]
for balloon in second_balloons:
    print("I got another " + balloon)

del balloon_colours[1:3] # delete 'blue' and 'purple'
print("Balloon colours still available: " + str(balloon_colours))

travel('walking') # function call
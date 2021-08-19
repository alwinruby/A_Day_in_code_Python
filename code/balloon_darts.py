# Balloon Darts program

balloons_popped = 5

if balloons_popped > 0 and balloons_popped <=2:
    dragon_size = "small"
elif balloons_popped >= 3 and balloons_popped < 5:
    dragon_size = "medium"
elif balloons_popped == 5:
    dragon_size = "large"
else:
    dragon_size = " "
    print("Try again!")

if dragon_size:
    print("You just won a " + dragon_size + " dragon!")

# Fireworks show program

# Function definition
def watch_fireworks():
    minutes = 0
    while True:
        minutes += 1
        if minutes < 15:
            continue # go back to the beginning of the loop

        minutes_left = 20 - minutes

        if minutes < 19:
            print("Amazing grand finale! Minutes Left: " + str(minutes_left))
        elif minutes == 19:
            print("One minute left!")
        elif minutes ==20:
            print("\nThat was a great fireworks show!\n")


sky = "not raining"

if sky != "raining":
    watch_fireworks()

print("Lets go home now!")
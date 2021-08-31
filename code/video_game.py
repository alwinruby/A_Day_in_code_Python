# Video game and cookies program.
video_game = input("What video game should we play? ")
print("OK, " + video_game.title() + " is a fun game.\n")

cookie_type = 'Chocolate Cookies'
if (cookie_type.lower() == 'chocolate cookies'):
    print("I love chocolate cookies!")

# Enter a numerical value (for example, 10 instaad of "ten")
bake_timer = input("How many minutes does it take to bake cookies? ")
bake_timer = int(bake_timer)

waiting = True
while waiting:
    if bake_timer == 0:
        waiting = False
    else:
        print("Timer: " + str(bake_timer))
        bake_timer -= 1 # This means bake_timer - 1

print("\nLet's play " + video_game.title() + " now!")
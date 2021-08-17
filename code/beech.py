#Beach program

flags = ('red', 'blue')
print("We have " + flags[0] + " & " + flags[1] + " flags for the sandcastles.")

pretzel_bag = "closed"
donut_box = "open"
building_sandcastle = True

if pretzel_bag == "open" or donut_box == "open": # outer if statement
    if building_sandcastle: # inner if statement
        print("\nSeagulls are eating")
    else:
        print("\nWatching out for Seagulls")
else:
    print("\nSeagulls are not eating")

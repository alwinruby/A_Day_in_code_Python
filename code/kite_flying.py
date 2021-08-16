# Kite flying program
print("There are four different kites available right now.\n")

kite_1 = {'shape': 'diamond-shaped', 'color': 'blue'}
kite_2 = {'shape': 'rectangular', 'color': 'green'}
kite_3 = {'shape': 'triangular', 'color': 'purple'}
kite_4 = {'shape': 'star-shaped', 'color': 'yellow'}

print("I'd like the " + kite_1['color'] + ", " + kite_1['shape'] + " kite")
print("I'd like the " + kite_3['color'] + ", " + kite_3['shape'] + " kite")

# Create a list of four dictionaries
kites_available = [kite_1, kite_2, kite_3, kite_4]

kites_available.remove(kite_1)
kites_available.remove(kite_3)

kites_left = len(kites_available)
print(str(kites_left) + " kites are left that have these features: ")
print(kites_available)

print("\nLet's fly our kites")

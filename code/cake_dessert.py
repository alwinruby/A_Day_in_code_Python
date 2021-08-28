# Cake for dessert program

class Dessert():
    """Modelling a dessert"""

    def __init__(self, size, cost):
        self.size = size
        self.cost = cost

    def about_dessert(self):
        print("\nThis " + self.size + " dessert is " + self.cost + ".")


class Cake(Dessert):
    """Modelling a dessert that is a cake."""

    def __init__(self, size, cost):
        super().__init__(size, cost)
        self.cake_type = "vanilla"

    def order_toppings(self, toppings):
        print("We would like these toppings on the cake: ")
        for topping in toppings:
            print(topping.title())


our_cake = Cake('large', '£20.00')
our_cake.cake_type = "chocolate"
print("We're ordering a " + our_cake.cake_type + "cake.\n")

cake_toppings = ('chocolate frosting', 'vanilla cream', 'sprinkles')
our_cake.order_toppings(cake_toppings)
our_cake.about_dessert()

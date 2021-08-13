# Breakfast programs

cook_time = 5
total_time = cook_time * 2
print("We made two waffles in " + str(total_time) + " minutes. \n")

waffle_toppings = ["strawberries", "banana slices", "blueberries", "raspberries"]

print("I like " + waffle_toppings[0] + " and " + waffle_toppings[1] + ".")
print("But let's add some more toppings. \n")

favorite_topping = "ice cream"
waffle_toppings.append(favorite_topping)
waffle_toppings.append("chocolate syrup")
waffle_toppings.append("powdered sugar")

print("These are all the toppings now:")
for topping in waffle_toppings:
    print(topping.title())


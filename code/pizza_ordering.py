# Pizza ordering program

# Function definitions

def pizza_type(size, crust):
    print("I would like a " + crust + "-crust, " + size + " pizza.")

def calculate_cost(total_pizzas, total_toppings, pizza_cost):
    total_cost = total_pizzas * pizza_cost + total_toppings * topping_cost
    return total_cost

# These variables have a float data type since the numbers have a decimal point
small_cost, medium_cost, large_cost, topping_cost = 4.99, 7.99, 9.99, 0.99

toppings = ("basil", "extra cheese", "pepperoni", "garlic", "peppers", "tomatoes")
print("We'd like the " + toppings[1] + " and " + toppings[3] + " toppings.")

#Function calls
pizza_type('medium', 'thick')
pizza_type(crust = 'crispy thin', size = 'medium')
total_pizza_cost = calculate_cost(2, 4, medium_cost)

print("\nThe total cost is £" + str(total_pizza_cost) + ". Enjoy!")
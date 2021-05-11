# Your code below:
# Checkpoint 1
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Checkpoint 2
prices = [2, 6, 1, 3, 2, 7, 2]

# Checkpoint 3
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Checkpoint 4
num_pizzas = len(toppings)

# Checkpoint 5
print("We sell", num_pizzas, "different kinds of pizza!")

# Checkpoint 6
# lines 20-21 for Checkpoint 12 
toppings.append("peppers")
prices.append(2.5)
pizza_and_prices = list(zip(prices, toppings))

# Checkpoint 7
#print(pizza_and_prices)

# Checkpoint 8
pizza_and_prices.sort()
#print(pizza_and_prices)

# Checkpoint 9
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)

# Checkpoint 10
priciest_pizza = pizza_and_prices[-1]
#print(priciest_pizza)

# Checkpoint 11
pizza_and_prices.remove(pizza_and_prices[-1])
#print(pizza_and_prices)

# Checkpoint 12
#adding lines 45-46 to Checkpoint 6 due to order of ops
#toppings.append("peppers")
#prices.append(2.5)
print(pizza_and_prices)

# Checkpoint 13
three_cheapest = pizza_and_prices[0:3]

# Checkpoint 14
print(three_cheapest)
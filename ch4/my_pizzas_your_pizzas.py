# 4-11 My Pizzas, Your Pizzas
pizzas = ["pepperoni", "margherita", "hawaiian"]
for pizza in pizzas:
    print(pizza)
    print("I like " + pizza + " pizza.\n")
print("I really love pizza!")

friend_pizzas = pizzas[:]
friend_pizzas.append("baiana")

print("My favorite pizzas are:")
print(pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

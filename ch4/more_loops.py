# 4-12 More Loops
my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(food)

my_foods.append("cannoli")
friends_foods.append("ice cream")

print("\nMy favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(food)

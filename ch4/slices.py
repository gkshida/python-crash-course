# 4-10 Slices
cubes = [number**3 for number in range(1, 11)]
print(f"The first three items in the list are: {cubes[:3]}")
print(f"Three items from the middle of the list are: {cubes[4:7]}")
print(f"The last three items in the list are: {cubes[-3:]}")

# 3-5  Changing Guest List
guests = ["Alice", "Bob", "Charlie"]
print(f"Hello, {guests[0]}! Please join me for dinner.")
print(f"Hello, {guests[1]}! Please join me for dinner.")
print(f"Hello, {guests[2]}! Please join me for dinner.")
print(f"Unfortunately, {guests[1]} can't make it to dinner.")
guests[1] = "David"
print(f"Hello, {guests[0]}! Please join me for dinner.")
print(f"Hello, {guests[1]}! Please join me for dinner.")
print(f"Hello, {guests[2]}! Please join me for dinner.")

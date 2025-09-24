the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "bananas"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# for循环
for number in the_count:
    print(f"这个数字是：{number}")

for fruit in fruits:
    print(f"这个水果是：{fruit}")

for c in change:
    print(f"change: {c}")


elements = []
for i in range(1, 11):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")

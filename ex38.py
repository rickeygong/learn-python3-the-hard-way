ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix it.")

stuff = ten_things.split(" ")
print(stuff)  # 打印：['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar']

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# stuff 长度不等于 10
while len(stuff) != 10:
    next_one = more_stuff.pop()  # 取 more_stuff 最后一个
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])  # Oranges
print(stuff[-1])  # Corn
print(stuff.pop())  # Corn，取最后一个，取完后会去掉
print(" ".join(stuff))
print(" ###### ".join(stuff[3:5]))


# l = ["a", "b", "c"]
# ls = "#.".join(l)
# print(ls)

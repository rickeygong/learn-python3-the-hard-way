things = ["a", "b", "c", "d"]
print(things[1])  # b
print(things[3])  # d

# 替换
things[0] = "k"
print(things)  # ['k', 'b', 'c', 'd']

print("===========================================")

# 定义字典（ Dictionary ）
stuff = {"name": "Donghai", "age": 18, "height": 100 + 30 * 2 + 5}
print(stuff["name"])  # Donghai
print(stuff["age"])  # 18
print(stuff["height"])  # 165

print(stuff)

stuff["city"] = "Shanghai"
print(stuff)  # {'name': 'Donghai', 'age': 18, 'height': 165, 'city': 'Shanghai'}

stuff["height"] = 180
print(stuff)  # {'name': 'Donghai', 'age': 18, 'height': 180, 'city': 'Shanghai'}

print("===========================================")

print(abs(-900))

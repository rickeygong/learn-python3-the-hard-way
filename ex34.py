# 定义列表
animals = ["bear", "tiger", "penguin", "zebra", "cat", "dog", "pig", "duck"]
bear = animals[0]

# 获取列表元素 —— 通过索引获取
print(f"获取第1个元素：{animals[0]}")
print(f"获取第3个元素：{animals[2]}")
print(f"获取最后一个元素：{animals[-1]}")

# 获取列表元素 —— 使用切片获取多个元素
print(f"获取从第二个到第四个元素（不包括第四个）：{animals[1:4]}")
print(f"获取从开始到第三个元素：{animals[:3]}")
print(f"获取从第四个到最后一个元素{animals[4:]}")

# 遍历列表
for i in animals:
    print(f"遍历列表：{i}")

# 使用 enumerate 获取索引和元素
for index, element in enumerate(animals):
    print(f"index: {index}, element: {element}")

# 检查元素是否在列表中
if "abc" in animals:
    print("abc 存在列表")
else:
    print("abc 不存在列表")

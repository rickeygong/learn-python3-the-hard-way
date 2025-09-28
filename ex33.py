i = 0
numbers = []  # 定义列表

while i < 6:
    print(f"(上）当前 变量i 是：{i}")
    numbers.append(i)  # 添加到 numbers 列表
    i = i + 1
    print(f"当前 列表 numbers 是：{numbers}")
    print(f"(下）当前 变量i 是：{i}")

print("while循环结束，打印 numbers 列表：")

for n in numbers:
    print(n)

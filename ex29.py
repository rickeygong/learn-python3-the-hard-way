# if 语句
x = 5

if x > 5:
    print("x 大于 5")
elif x == 5:
    print("x 等于 5")  # 这行代码会被执行
else:
    print("x 小于 5")

print("--------------")

y = 10

if y > 5:
    print("y 大于 5")
    if y > 8:
        print("y 还大于 8")  # 这行会被执行

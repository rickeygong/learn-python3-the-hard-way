print("怎么称呼你？", end="")
name = input()

print("你多少岁了？", end="")
age = input()

print("你的身高是多少厘米？", end="")
height = input()

print("你的体重是多少公斤？", end="")
weight = input()

print(
    f"{name}，你好！感谢你告诉我怎么多信息，我知道了你的年龄：{age}岁，身高是{height}厘米，体重是{weight}公斤"
)

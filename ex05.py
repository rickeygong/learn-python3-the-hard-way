# 变量赋值
name = "龚东海"  # 字符串
age = 18  # 整数
height = 165.5  # 浮点数
is_student = False  # 布尔型

# 输出变量的值
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# 变量计算
new_age = age + 20
print(f"20年后的岁数是: {new_age}")

# 变量交换
x = 10
y = 20
print(f"变量交换前: x = {x}，y = {y}")

# 使用表达式
a = 10
b = 5
print(f"The sum of {a} and {b} is {a + b}.")
print(f"{name} will be {age + 1} next year.")

# 交换 x 和 y 的值
x, y = y, x
print(f"变量交换后: x = {x}，y = {y}")

c = 100
d = 3
result = c / d
print(f"100 / 3 = {result:.2f}")

def add(a, b):
    print(f"加法 {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"减法 {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"乘法 {a} * {b}")
    return a * b


def divide(a, b):
    print(f"除法 {a} / {b}")
    return a / b


print("调用函数做简单的数学运算")

age = add(10, 8)
height = subtract(180, 15)
weight = multiply(15, 10)
iq = divide(200, 2)

print(
    f"""
    年龄：{age}
    身高：{height}
    体重：{weight}
    IQ：{iq}
    """
)

# 还可以函数套函数

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")

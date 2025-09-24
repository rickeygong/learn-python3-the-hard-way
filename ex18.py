# 变量，代码，函数

# def --> define，定义的意思


def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2:{arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")


def print_one(arg1):
    print(f"arg1:{arg1}")


def print_none():
    print("没有参数的函数")


print_two("罗伯特", "索尼娅")
print_two_again("李晓明", "黄太明")
print_one("韩东君")
print_none()

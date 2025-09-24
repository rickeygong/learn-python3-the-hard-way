print("练习一下前面的内容")
print("你需要知道关于转义字符，\\ 它们有：")
print("\n 换行，\t 制表符")

poem = """
\t月照松间影，风吟竹外声
云间孤雁鸣
山色渐苍茫 \n 碧空如洗日
寒山夜雨声，灯下独坐思
归鸟逐云飞
\n\t\t梅花点点香。
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print(f"这应该是：{five}")


def secret_formula(started):
    var_1 = started * 500
    var_2 = var_1 / 1000
    var_3 = var_2 / 100
    return var_1, var_2, var_3


start_point = 10000
var_1, var_2, var_3 = secret_formula(start_point)

# 记住，这也是格式化字符串的另一种方式
print("起始点为：{}".format(start_point))
# 这就像使用 f"" 字符串一样
print(f"我们将拥有 {var_1} 颗豆子，{var_2} 罐，和 {var_3} 箱。")

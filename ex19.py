# 函数和变量


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"你有{cheese_count}块奶酪")
    print(f"你有{boxes_of_crackers}盒饼干")
    print(f"吃怎么多甜食，小心高血压")
    print(f"来人啊，给他上一瓶大可乐")


# 调用函数
cheese_and_crackers(20, 15)

# 调用函数（变量）
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 调用函数（含变式）
cheese_and_crackers(2 + 3, 20 - 8)

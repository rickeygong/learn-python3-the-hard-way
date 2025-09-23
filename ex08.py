formatter = "{} {} {} {}"

print(formatter.format(100, 200, 300, 400))
print(formatter.format("你", "好", "啊", "！"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(
    formatter.format(
        "今天是2025年9月23日",
        "我还在上班",
        "明天再上一天班就可以放假了",
        "因为周四和周五请假",
    )
)

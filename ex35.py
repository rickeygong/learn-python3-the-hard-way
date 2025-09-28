from sys import exit


def gold_room():
    print("这里有一堆金子，你要拿多少？")
    choice = input(">>> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("大兄弟，请输入一个数字")

    if how_much < 100:
        print("不错，那这些不算贪婪")
        exit(0)
    else:
        print("你这个贪婪的家伙")


def bear_room():
    print("这里有一只熊")
    print("这里有一群蜜蜂")
    print("这只熊堵在门口了")
    print("你打算怎么办？")
    bear_moved = False

    while True:
        choice = input(">>> ")
        if choice == "拿蜂蜜":
            dead("熊给了你一巴掌")
        elif choice == "挑衅熊" and not bear_moved:
            print("熊已经走开了")
            print("你现在可以通过，赶紧跑")
            bear_moved = True
        elif choice == "挑衅熊" and bear_moved:
            print("熊生气了，咬了你的腿")
        elif choice == "打开门" and bear_moved:
            gold_room()
        else:
            print("我不知道这是什么意思，或许你该说点人话")


def dead(why):
    print(why, "干得好！")
    exit(0)


def cthulhu_room():
    print("你看到了一个黢黑的巫师")
    print("Ta散发出不可描述的臭味")
    print("你要逃跑，还是继续探险？")
    choice = input(">>> ")
    if "逃跑" in choice:
        start()
    elif "探险" in choice:
        dead("嗯，真好吃...来自巫师的细语...你已经被吃了...")
    else:
        cthulhu_room()


def start():
    print("你在一个黑暗的房间里")
    print("你右边和左边都有一扇门")
    print("你要走哪一扇门？")
    choice = input(">>> ")
    if choice == "左":
        bear_room()
    elif choice == "右":
        cthulhu_room()
    else:
        dead("你在房间里乱撞，直到饿死")


start()

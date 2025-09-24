# 阅读文件
from sys import argv

script, filename = argv  # 获取文件名

# txt = open(filename) 会返回文件的内容吗？
# 不会。它其实是创建了一个叫做“文件对象”（file object）的东西。
# 你可以把它想象成曾经的 DVD 播放器，你可以在里面移动然后“读取”它们。
# 但是 DVD 播放器不是 DVD 本身，就像文件对象也不是文件本身一样
txt = open(filename, encoding="utf-8")

print(f"这个是你打开的文件：{filename}")
print(txt.read())

print("请再次输入文件名：")
file_again = input(">>> ")

txt_agin = open(file_again, encoding="utf-8")
print(txt_agin.read())

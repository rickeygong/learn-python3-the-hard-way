# 读写文件
# close - 关闭文件，就像编辑器中的 “文件->另存为”一样
# read - 读取文件内容。你可以把读取结果赋给一个变量
# readline - 只读取文本文件的一行内容
# truncate - 清空文件。清空的时候要当心
# write('stuff') - 给文件写入一些“东西”
# seek(0) - 把读/写的位置移到文件最开头

from sys import argv

script, filename = argv

print(f"我们将删除{filename}文件")
print("如果你不想删除，请按 Ctrl + C")
print("如果你确定删除，请按 Enter")

input("?")

print("正在打开文件中...")
target = open(filename, "w", encoding="utf-8")

# 读取前3行内容
# target = open(filename, "r", encoding="utf-8")
# print(target.readline())
# print(target.readline())
# print(target.readline())

print("正在清空文件内容...")
target.truncate()  # truncate - 清空文件内容

print("现在我想请你写3句话：")

line1 = input("第1句：")
line2 = input("第2句：")
line3 = input("第3句：")

print(f"现在我要把这3句话写到{filename}文件中...")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"这3句话已经添加完了，你可以打开 {filename} 看看写入的内容")

target.close()

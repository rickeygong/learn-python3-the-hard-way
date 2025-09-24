from sys import argv
from os.path import exists  # 导入 exists 函数，用于检查文件或目录是否存在

script, from_file, to_file = argv  # 接收参数

# 打印出复制操作的信息，告知用户将从哪个文件复制到哪个文件
print(f"将{from_file}文件拷贝到{to_file}文件")

# 以默认模式（只读）打开源文件 from_file，并将文件对象赋值给 in_file
in_file = open(from_file, encoding="utf-8")

# 读取源文件的所有内容，并将其存储在变量 indata 中
indata = in_file.read()

print(f"{from_file}文件长度是{len(indata)}")
print(f"{to_file}文件是否存在？—— {exists(to_file)}")

print("我已经准备就绪，接下来请你给出指示：")
print(">>> 继续：按 Enter")
print(">>> 退出：按 Ctrl + C")
input()

# 以写模式打开目标文件 to_file，如果文件已存在，则会被清空
out_file = open(to_file, "w", encoding="utf-8")

# 将从源文件读取到的内容写入目标文件
out_file.write(indata)

print("已经拷贝好了！")

# 关闭源文件，释放资源
out_file.close()
in_file.close()

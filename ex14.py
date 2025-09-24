# Prompting and Passing
# 让我们来做一个把 argv 和 input 结合在一起的练习来问用户一些特别的问题

from sys import argv

script, user_name = argv
prompt = ">>>> "

print(f"你好啊，{user_name}，我是这个剧本的作者")
print("我现在想问你几个问题")
print(f"{user_name}，你喜欢我吗？")
likes = input(prompt)

print(f"{user_name}，你现在住在哪里？")
lives = input(prompt)

print(f"你喜欢用什么牌子的电脑啊？")
computer_brand = input(prompt)

print(
    f"""
    很好，我知道你{likes}我了，而且还知道你喜欢使用{computer_brand}品牌的电脑
    但是你居住的地方（{lives}）我还没有听说过
      """
)

print(f"True and True: {True and True}")
print(f"False and True: {False and True}")
print(f"1 == 1 and 2 == 1: {1 == 1 and 2 == 1}")
print(f"\"test\" == \"test\": {'test' == 'test'}")  # 使用单引号
print(f"1 == 1 or 2 != 1: {1 == 1 or 2 != 1}")
print(f"True and 1 == 1: {True and 1 == 1}")
print(f"False and 0 != 0: {False and 0 != 0}")
print(f"True or 1 == 1: {True or 1 == 1}")
print(f"\"test\" == \"testing\": {'test' == 'testing'}")  # 使用单引号
print(f"1 != 0 and 2 == 1: {1 != 0 and 2 == 1}")
print(f"\"test\" != \"testing\": {'test' != 'testing'}")  # 使用单引号
print(f"\"test\" == 1: {'test' == 1}")  # 使用单引号
print(f"True and False: {not (True and False)}")
print(f"not (1 == 1 and 0 != 1): {not (1 == 1 and 0 != 1)}")
print(f"not (10 == 1 or 1000 == 1000): {not (10 == 1 or 1000 == 1000)}")
print(f"not (1 != 10 or 3 == 4): {not (1 != 10 or 3 == 4)}")
print(
    f"not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\"): {not ('testing' == 'testing' and 'Zed' == 'Cool Guy')}"
)
print(
    f"1 == 1 and (not (\"testing\" == 1 or 1 == 0)): {1 == 1 and (not ('testing' == 1 or 1 == 0))}"
)
print(
    f"\"chunky\" == \"bacon\" and (not (3 == 4 or 3 == 3)): {'chunky' == 'bacon' and (not (3 == 4 or 3 == 3))}"
)  # 使用单引号
print(
    f"3 == 3 and (not (\"testing\" == \"testing\" or \"Python\" == \"Fun\")): {3 == 3 and (not ('testing' == 'testing' or 'Python' == 'Fun'))}"
)

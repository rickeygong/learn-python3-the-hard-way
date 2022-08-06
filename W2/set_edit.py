# coding:utf-8

a_list = ['python','django','django','flask']

a_set = set()

a_set.add(a_list[0])
a_set.add(a_list[1])
a_set.add(a_list[2])
a_set.add(a_list[-1])

print(a_set) # {'flask', 'python', 'django'}

a_set.add(True)
a_set.add(None)
print(a_set) # {'python', True, None, 'flask', 'django'}


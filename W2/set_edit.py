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

a_tuple = ('a','b','c')
a_set.update((a_tuple))
print('print:',a_set)
a_set.update('RICKEY')
print(a_set)
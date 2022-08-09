# coding:utf-8

drivers = ['dewei','xiaomu','xiaoming','xiaoman']
testers = ['xiaomu','xiaoman','xiaogang','xiaotao']

drivers_set = set(drivers)
testers_set = set(testers)

sample_drivers = drivers_set.difference(testers_set)
print(sample_drivers)
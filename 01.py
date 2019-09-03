# -*- encoding: utf-8 -*-
"""
寻找水仙花数

@File    : 01.py
@Time    : 2019/8/28 9:15
@Author  : HeKai
@Email   : hek@corp.21cn.com
@Software: PyCharm
"""

num = int(input('请输入'))
list = []
for i in range(1, num):
    sum = 0
    tmp = i
    while tmp != 0:
        sum += (tmp % 10) ** 3
        tmp = tmp // 10
    if sum == i:
        list.append(i)

print("%d以内的水仙花数为：" % num)
for j in list:
    print(j)


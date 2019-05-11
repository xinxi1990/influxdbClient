#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
filter过滤
"""


# def is_odd(n):
#     return n % 2 == 1
#
# newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(list(newlist))



a = filter(lambda x: x % 2 == 0, range(10))
print(list(a))

a_list = [ i* i for i in range(1,11) if i % 2 == 0 ]
print(a_list)
# 列表推导式

a_num = {}
a_dict= {"a":1,"b":2}
for i in  a_dict:
    a_num[i] = 0
print(a_num)

a_num = { i:0 for i in a_dict }
print(a_num)
# 字典推导式



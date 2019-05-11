#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
file io
"""


# with open("test.txt","a") as  f:
#     for i in range(100):
#         f.write("this is test:{}".format(i) + "\n")


with open("test.txt") as  f:
       print(f.tell())
       print(f.read())
       print(f.tell())
       f.seek(50,0)
       print(f.read())
       # 回到开头,再次进行操作
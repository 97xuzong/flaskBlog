#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : dict_.py
# @Time    : 2023/1/4 20:03
# @Software: PyCharm
# @function: 字典的常用方法

dict1 = {"name": "张三", "address": "湖北"}

# sort是列表的默认方法   但是sorted是独立的方法
res_dict = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
print(isinstance(res_dict[0], tuple))
print(res_dict[0])

res1 = zip(dict1.keys(), dict1.values())
print(type(res1))
res1_1 = sorted(res1)
print(res1_1)

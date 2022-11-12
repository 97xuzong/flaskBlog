#  -*- coding: utf-8 -*-
# @Author  : ymnl
# @File    : call_back_func.py
# @Time    : 2022/11/12 23:48
# @Software: PyCharm
# @function: 回调函数 ： 函数当作其他函数的入参

def get_avg(x, y):
    return (x + y) / 2


def get_sum(x, y):
    return (x + y)


def choose(func, x, y):
    return func(x, y)


print(choose(get_avg, 10, 20))
print(choose(get_sum, 10, 20))

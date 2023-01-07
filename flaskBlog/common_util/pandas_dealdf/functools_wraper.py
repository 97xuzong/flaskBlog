#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : functools_wraper.py
# @Time    : 2022/12/9 23:56
# @Software: PyCharm
# @function: py3.8以后版本自带了一个封装好的装饰器

from functools import wraps


def wraper(func):
    '''装饰器类的注释'''
    @wraps(func)
    def inner(*args):
        print("新增开始")
        res = func(args)
        print("新增结束")
        return res

    return inner


@wraper
def my_func(*args):
    '''真的是及其幼稚  真的都是有点无语'''
    print(f"我的参数是{args}")
    return "success"


resp = my_func('张三', '李四', '王五')
print(my_func.__name__, my_func.__doc__)

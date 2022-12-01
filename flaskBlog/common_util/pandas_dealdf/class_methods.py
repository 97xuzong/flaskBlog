#  -*- coding: utf-8 -*-
# @Author  : ymnl
# @File    : class_methods.py
# @Time    : 2022/11/28 17:06
# @Software: PyCharm
# @function: 类方法

class Test(object):
    count_ = 0

    def __init__(self, name):
        self.name = name

    # 类方法只能访问类变量  不能访问实例变量
    @classmethod
    def wocao(cls):
        print("类方法只能访问类变量  不能访问实例变量等",cls.count_)

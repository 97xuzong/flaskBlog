#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : magic_methods.py
# @Time    : 2022/12/10 23:06
# @Software: PyCharm
# @function:

class YuKl(object):
    # def __new__(cls, *args, **kwargs):
    #     return object()
    count_ = 0

    def __init__(self):
        self.name = "张三"

    def __repr__(self):
        return "直接输出对象的时候执行"

    @classmethod
    def cls_vars_use(cls):
        cls.count_ += 1
        return cls.count_

    @staticmethod
    def utils(*args):
        return sum(args)


print(YuKl())
obj = YuKl().utils(1, 2, 3, 4)
print(obj)

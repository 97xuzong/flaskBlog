#  -*- coding: utf-8 -*-
# @Author  : ymnl
# @File    : singalSample.py
# @Time    : 2022/11/28 16:14
# @Software: PyCharm
# @function: 单例模式

class Ehansi(object):
    instance_ = None

    def __new__(cls, *args, **kwargs):
        if cls.instance_ is None:
            cls.instance_ = object.__new__(cls)
            return cls.instance_
        else:
            return cls.instance_


obj1 = Ehansi()
obj2 = Ehansi()

print(obj1 is obj2)

#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : func_args.py
# @Time    : 2022/12/2 17:05
# @Software: PyCharm
# @function: 函数中的备用参数用None赋值后可不传参


def test(num1,flag=None):
    flag = flag if flag else 1
    print(num1+flag)


test(100,20)

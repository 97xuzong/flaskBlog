#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : nobecome.py
# @Time    : 2023/1/2 17:03
# @Software: PyCharm
# @function: 字符串不可变值的是字符串对象创建之后  内容不可以改变  有的只是在改变其地址 指向不同的new 对象而已
#   用来保证程序中的对象固定不变
import datetime

str1 = "gddfe"
print(id(str1))
# str1[:2] = ""
str1 = "卧槽"
print(id(str1))

now = datetime.datetime.now()
print(now.month)
first = datetime.datetime(now.year, now.month, 1)
first = first - datetime.timedelta(days=1)
second = datetime.datetime(first.year, first.month, 1)
res = second - datetime.timedelta(days=1)
print(str(res.year) + str(res.month) + str(res.day))

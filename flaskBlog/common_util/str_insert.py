#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : str_insert.py
# @Time    : 2023/1/5 22:12
# @Software: PyCharm
# @function: python中的字符串内容不可变 不能进行插入和删除


str1 = "缝合个."
index1 = str1.index(".")
print(index1)

list1 = list(str1)
print(list1)

# for循环按照从大到小 并按照指定步长进行递减 循环
#  1234343.09 -> 1,234,343.09  标准计数格式
str2 = "1234343.09"
list2 = list(str2)
for i in range(list2.index(".") - 3, 0, -3):
    if i > 0:
        list2.insert(i, ",")
    else:
        break
res = "".join(list2)
print(res)

str_demo = "这是一首简单的小情歌"
# str_demo.replace()
print(len(str_demo))
print(str_demo[:8:2])
print(id(str_demo))
# 重新赋值只是指向了新创建的对象 原有的 这是一首简单的小情歌  依然会存在内存中 有垃圾回收机制管理
str_demo += "；我从单位"
print(id(str_demo))

#
str_demo1 = "过分单位"
print(id(str_demo1))
str_demo1 = str_demo1.replace("单位","dw")
print(id(str_demo1))


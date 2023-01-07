#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : buddle.py
# @Time    : 2022/12/10 23:13
# @Software: PyCharm
# @function: 手写一个冒泡排序并优化

def buddle_sort(list1: list) -> list:
    for i in range(len(list1) - 1):
        flag = True
        for j in range(len(list1) - 1 - i):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                flag = False
        if flag:
            print(f"第{i + 1}轮完成升序排列的序列")
            break

    return list1


print(buddle_sort([1, 2, 10, 11, 100]))

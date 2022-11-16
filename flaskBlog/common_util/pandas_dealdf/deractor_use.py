#  -*- coding: utf-8 -*-
# @Author  : ymnl
# @File    : deractor_use.py
# @Time    : 2022/11/13 18:23
# @Software: PyCharm
# @function: 装饰器实现登录权限
from functools import wraps
import pandas as pd


def wrapper(func):
    """ 装饰器函数"""

    @wraps(func)
    def inner(*args):
        if args == "admin":
            return func(*args)
        else:
            return "没有登陆权限"

    return inner


@wrapper
def login(name):
    """被装饰函数"""
    return f"{name}已登录"


print(login("admin"))
print(login.__name__, login.__doc__)

df = pd.DataFrame(data={"name": ['a', 'b', 'b'], "address": ['eng', 'china', 'ameical']})
df1 = df.groupby("name", as_index=False).address.apply(lambda x: "-".join(list(x)))
print(df1)

# pop直接获取字典的值 并删除原有对应的键值对
dict1 = {"name": "zhangsan", "age": 34}
print(dict1.pop("name"), dict1)

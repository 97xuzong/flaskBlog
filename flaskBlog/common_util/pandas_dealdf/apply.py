#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : apply.py
# @Time    : 2022/12/1 9:52
# @Software: PyCharm
# @function: apply中的axis问题
import json

import pandas as pd

'''apply是将df拆分为series进行处理
    1.axis=0 默认，是将一列的所有行组成series
    2.axis=1 一行的所有列组成series
'''


def deal_func(series):
    return (series > 250).sum()


data = [[100, 200, 300, 400], [200, 150, 340, 250]]
df = pd.DataFrame(data=data, columns=["m1", "m2", "m3", "m4"])
df[">250"] = df.apply(deal_func, axis=1)
print(df)

"""
    m1   m2   m3   m4  >250
0  100  200  300  400     2
1  200  150  340  250     1
"""

res1 = pd.DataFrame(df)
print(res1)

print("感觉自己最近特别浮躁  这种感觉其实是有点不爽的  你知道吧")

from urllib.parse import quote

# 将字符串‘程序设计’进行编码
text = quote("家电", 'utf-8')
print(text)
# 打印结果
# %E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1

dict1 = {"data":"{\"name\":\"dwddwdw\"}"}
print(json.dumps(dict1))
#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : dict_empty.py
# @Time    : 2022/12/8 14:09
# @Software: PyCharm
# @function: 可以通过长度来判断字典是否为空
import pandas as pd
import numpy as np

dict1 = {}
print(dict1.__len__())
df = pd.DataFrame(data={"name": ['张三', '李四'], "address": ['湖北', np.NaN]})
df.fillna('', inplace=True)
print(df.to_dict("records"))

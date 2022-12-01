#  -*- coding: utf-8 -*-
# @Author  : ymnl
# @File    : reindex.py
# @Time    : 2022/11/26 18:51
# @Software: PyCharm
# @function: reindex

import pandas as pd

df = pd.DataFrame(data={"name": ["张三", "李四"], "address": ["湖南", "湖北"]})
df1 = df.reindex(columns=["name", "c", "d"], fill_value="xxxx")
print(df1)

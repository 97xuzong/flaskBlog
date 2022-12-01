#  -*- coding: utf-8 -*-
# @Author  : ymnl
# @File    : df_to_dict.py
# @Time    : 2022/11/22 16:15
# @Software: PyCharm
# @function: df to dict

import pandas as pd

df = pd.DataFrame(data={"name":['a','b'],"address":['china','england']})
res = df.to_json(orient="records")
res1 = df.to_dict(orient="records")
print(res)
print(res1)

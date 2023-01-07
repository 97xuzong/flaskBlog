#  -*- coding: utf-8 -*-
# @Author  : ymnl
# @File    : reindex.py
# @Time    : 2022/11/26 18:51
# @Software: PyCharm
# @function: reindex
from datetime import datetime
from datetime import timedelta
import dateutil
import pandas as pd

df = pd.DataFrame(data={"name": ["张三", "李四"], "address": ["湖南", "湖北"]})
df1 = df.reindex(columns=["name", "c", "d"], fill_value="xxxx")
print(df1)

import dateutil


def before_month_lastday():
    now = datetime.now()
    first = datetime(now.year, now.month, 1)
    lastMonth = first - timedelta(days=1)
    cc = str(lastMonth.year) + str(lastMonth.month) + str(lastMonth.day)
    return int(cc)


print(before_month_lastday())

print(type(datetime.strftime(datetime.now(),"%Y%m%d")))
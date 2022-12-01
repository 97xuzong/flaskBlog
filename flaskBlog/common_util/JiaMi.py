#  -*- coding: utf-8 -*-
# @Author  : ymnl
# @File    : JiaMi.py
# @Time    : 2022/11/22 11:09
# @Software: PyCharm
# @function:

import hashlib

res = hashlib.md5()
str = 'boboadmin'
res.update(str.encode())
msg = res.hexdigest()
print(msg)

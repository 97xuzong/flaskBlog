#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : json_dict.py
# @Time    : 2023/1/7 22:56
# @Software: PyCharm
# @function: json有关用法

import json

json1 = '''{"name":"zs"}'''
json2 = "{'address':'lundon'}"

# loads将字符串转字典的时候 字典中的键值对必须是双引号 "",最终的字典为单引号 ''
dict1 = json.loads(json1)
print(dict1)
# dict2 = json.loads(json2)

# dumps 将字典转字符串  遇到中文编码问题后可用en....= False
dict_2 = {"name": "zs"}
dict_3 = {'address': 'lundon'}
str1 = json.dumps(dict_2)
str2 = json.dumps(dict_3)
print(str1)
print(str2)

print(json.loads(str2))

dict_res = {"name":"张三"}
res_str1 = json.dumps(dict_res,ensure_ascii=False)
res_str2 = json.dumps(dict_res)
print(res_str1)
print(res_str2)
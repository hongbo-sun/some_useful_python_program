#coding:utf-8
from urllib import request
from urllib.parse import quote
import urllib
import json
import numpy as np
import pdb


input_entity_name = quote('红富士')
print("ping1")
pdb.set_trace()
input_attr = quote('英文名称')

#input_url = 'http://shuyantech.com/api/cndbpedia/ment2ent?q='
# 输入实体指称项名称，返回对应实体(entity)的列表，json格式
# 格式http://shuyantech.com/api/cndbpedia/avpair?q=**      # **是查询的实体名
print("ping2")
pdb.set_trace()
input_url =  'http://shuyantech.com/api/cndbpedia/avpair?q='

#输入实体名，返回实体全部的三元组知识
#格式：http://shuyantech.com/api/cndbpedia/value?q=**&attr=**    # 前**是查询的实体名；后**是查询的属性名
#input_url = 'http://shuyantech.com/api/cndbpedia/value?q='
#url = input_url+input_entity_name+'&attr='+input_attr

print("ping3")
pdb.set_trace()
url = input_url+input_entity_name
response = urllib.request.urlopen(url)


print(response.read().decode('utf-8'))

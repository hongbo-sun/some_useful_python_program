# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 11:06:36 2019

@author: hongb
"""

import re



import urllib
from urllib import request
import _pickle as cPickle
from pytube import YouTube




headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}





res=[]
with open ('.\\3D.txt','r') as f:
    for line in f:
        res.append(line.split(' ')[1])
        
print(res)
print()
print(len(res))
print()
print('--------------------------------------------')



cPickle.dump(res,open(".\\3D.pkl","wb"))



count_right=0
count_wrong=0
countall=0
wrongdict={}

for urlname in res:
    urlname=re.sub('[\r\n\t]', '', urlname)
    print(urlname)
    try:
        req = urllib.request.Request(url=urlname, headers=headers)
        response=urllib.request.urlopen(req)
        
        
        #response = request.urlopen(urlname,timeout=5)
        print("可访问")
        count_right=count_right+1
    
    except:
        count_wrong=count_wrong+1
        wrongdict[count_wrong]=urlname
        print("错误")
    
    
    countall=countall+1
    
    print('--------------------------------------------')




print('wrong num')
print(count_wrong)
cPickle.dump(wrongdict,open(".\\3Dwrongdict.pkl","wb"))




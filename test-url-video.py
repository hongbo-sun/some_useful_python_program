# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 11:06:36 2019

@author: hongb
"""

from urllib import request
import _pickle as cPickle
import sys
from pytube import YouTube
import re








res=[]
with open (r'.\\video.txt','r') as f:
    for line in f:
        res.append(line.split(' ')[1])
        
print(res)
print()
print(len(res))
print('--------------------------------------------')

cPickle.dump(res,open(".\\videowebsite.pkl","wb"))



count_right=0
count_wrong=0
countall=0
wrongdict={}

for urlname in res:
    
    urlname=re.sub('[\r\n\t]', '', urlname)
    print(urlname)
    
    
    try:

        #response = request.urlopen(urlname)
        yt=YouTube(urlname)
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
cPickle.dump(wrongdict,open(".\\videowrongdict.pkl","wb"))




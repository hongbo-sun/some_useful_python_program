# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:00:00 2019

@author: hongb
"""


import sys
import random


res=[]



'''
list1=[]
for i in range (100):
    list1.append(random.randint(1001,2000))
'''








with open (r'C:\Users\hongb\Desktop\3D.txt','r') as f:
    for line in f:
        res.append(line.split(' ')[1])
print(res)









with open (r'C:\Users\hongb\Desktop\3D_new.txt','w') as f:
    for i in range(len(res)):
        f.write(res[i])
    
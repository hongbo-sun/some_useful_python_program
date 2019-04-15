# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:10:16 2019

@author: hongb
"""

# -*- coding: cp936 -*-
import re
import linecache
import numpy as np
import os
import scipy.io as io
 
filename = 'C:\\Users\\hongb\\Desktop\\fake_caption_BOW\\flickr\\flickr_bow_3000.txt'
 
 
def txt_strtonum_feed(filename):
    data = []
    with open(filename, 'r') as f:#with语句自动调用close()方法
        line = f.readline()
        while line:
            eachline = line.split()###按行读取文本文件，每行数据以列表形式返回
            read_data = [ float(x) for x in eachline ] 

           
            #read_data = list(map(float, eachline))
            data.append(read_data)
            line = f.readline()
        return data #返回数据为双列表形式


 
if __name__ == '__main__':
    
    '''
    test_content = txt_strtonum_feed(filename)
    content = np.array(test_content)
    print (content) 
    '''
    
    data=content[145000:][:]
    
    io.savemat('./f30k_test.mat', {'data':data })
    
    
    
    
    
    
    
    
    
    
    
    
 

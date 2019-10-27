# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:35:18 2019

@author: hongb
"""

import _pickle as cPickle

list1=['hello']

cPickle.dump(list1,open(".\\videowrongdict.pkl","wb"))

data = cPickle.load(open(".\\videowrongdict.pkl","rb")) 

print(data)


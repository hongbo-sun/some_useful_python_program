# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 11:55:45 2024

@author: Admin
"""
import os
import shutil

path = "D:\孙宏博个人文件\孙宏博博士毕业文件和入职文件整理-20240702"
keyword = "A1"

# 获取目标路径的绝对路径，并在路径前加上\\?\，
# 以解除windows的文件长度限制
path = '\\\\?\\' + os.path.abspath(path)

for root, dirs, files in os.walk(path):
    for dir in dirs:

        rmpath = os.path.join(root, dir)
        print("删除文件夹: %s" % rmpath)
        shutil.rmtree(rmpath)
            
            
            
    for file in files:

        rmpath = os.path.join(root, file)
        print("删除文件: %s" % rmpath)
        os.remove(rmpath)

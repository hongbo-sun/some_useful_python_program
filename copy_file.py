# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:39:50 2021

@author: hongbo
"""
import json

import os

from shutil import copyfile
import shutil

trian_file_list = "need_test_list.json"
source_folder="..\\test"
target_file = '.\\test_video\\'






with open(trian_file_list,'r') as load_f:
    load_dict = json.load(load_f)
   



for i in range(len(load_dict)):
    file = load_dict[i][1]

    try:
        file_name = file+'.webm'
        source_file = source_folder+'\\'+file_name
        shutil.copy(source_file, target_file)
        print(file_name)
        

    except :
        file_name = file+'.mp4'
        source_file = source_folder+'\\'+file_name
        shutil.copy(source_file, target_file)
        print(file_name)
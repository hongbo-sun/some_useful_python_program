# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 10:43:17 2024

@author: Admin
"""

import os  
import shutil  
  
def rename_images(folder_path, start_number=1):  
    # 获取文件夹中所有文件的列表  
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]  
      
    # 假设我们按照文件名排序（可以根据需要调整排序逻辑）  
    files.sort()  
      
    # 准备新的文件名  
    for index, file in enumerate(files, start=start_number):  
        # 构造新的文件名，例如'001.jpg'  
        new_name = f"{index:03d}{os.path.splitext(file)[1]}"  
        # 构造新文件的完整路径  
        #new_name = './new/'+new_name
        new_path ='./new/'+new_name
        # 构造原文件的完整路径  
        old_path = os.path.join(folder_path, file)  
          
        # 重命名文件  
        shutil.move(old_path, new_path)  
        print(f"Renamed '{file}' to '{new_name}'")  
  
# 使用示例  
folder_path = './old/'  # 替换为你的图片文件夹路径  
rename_images(folder_path)
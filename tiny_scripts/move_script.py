import os
import sys
import shutil

# 从 origin_path 文件夹中移动指定后缀文件到 target_path 文件夹中

origin_path = 'E:\\学习课件\\数字图像分析\\第三次作业-图象表征\\Image\\'

target_path = 'E:\\学习课件\\数字图像分析\\第三次作业-图象表征\\sift'

file_type = '.dsift'

for file in os.listdir(origin_path):
    if file.endswith(file_type):
        shutil.move(origin_path + file, target_path)
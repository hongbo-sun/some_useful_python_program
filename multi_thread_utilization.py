# -*- coding: UTF-8 -*-
import os, subprocess, threadpool

def run_sh(sh_filepath):
    log_filepath = os.path.join('./logs', sh_filepath.replace('.sh', '.log'))
    error_filepath = os.path.join('./logs', sh_filepath.replace('.sh', '_caffe.log'))
    subprocess.call('sh ' + sh_filepath, shell = True, stdout = open(log_filepath, 'a'), stderr = open(error_filepath, 'a'))
    print(sh_filepath + '已完成')

sh_filepath_list = ['extractfea_txt_vgg16_topics_N5_image_neg.sh', 
                    'extractfea_txt_vgg16_topics_N5_image_pos_new.sh',
                    'extractfea_txt_vgg16_topics_N5_video_neg_00.sh',
                    'extractfea_txt_vgg16_topics_N5_video_neg_01.sh',
                    'extractfea_txt_vgg16_topics_N5_video_neg_02.sh',
                    'extractfea_txt_vgg16_topics_N5_video_neg_03.sh',
                    'extractfea_txt_vgg16_topics_N5_video_pos.sh']

pool = threadpool.ThreadPool(7)
reqs = threadpool.makeRequests(run_sh, sh_filepath_list) 
[pool.putRequest(req) for req in reqs]
pool.wait()


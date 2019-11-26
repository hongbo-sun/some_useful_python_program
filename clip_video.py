# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:21:50 2019

@author: hongbo
"""



import cv2
import scipy.io as sio


load_data = sio.loadmat('./sel_neg_videoIds.mat')
#print (load_data['sel_neg_videoIds'][1][0][0])

header='/data1/zhangjunchao/workspace/Caption/dataset/MSRVTT/train-video/'
tail='.mp4'




outheader='./'
outtail1='_1.mp4'
outtail2='_2.mp4'
#print (header+load_data['sel_neg_videoIds'][1][0][0].split('/')[1]+tail)

for i in range(1024):
    
    capvideo=header+load_data['sel_neg_videoIds'][i][0][0].split('/')[1]+tail
    
    outvideo1=outheader+load_data['sel_neg_videoIds'][i][0][0].split('/')[1]+outtail1
    outvideo2=outheader+load_data['sel_neg_videoIds'][i][0][0].split('/')[1]+outtail2
    

    
    cap = cv2.VideoCapture(capvideo)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps =cap.get(cv2.CAP_PROP_FPS)
    
    
    
    frames_num=cap.get(7)
    #print (frames_num)
    
    
    
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
    out1 = cv2.VideoWriter(outvideo1,fourcc, fps, size)
    out2 = cv2.VideoWriter(outvideo2,fourcc, fps, size)
    
    
    num=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret==True:
            
            
            #frame = cv2.flip(frame,0)
            
            
            if num<frames_num/2:
                out1.write(frame)
            else:
                out2.write(frame)
              
                
                
            
           #cv2.imshow('frame',frame)
           #if cv2.waitKey(1) & 0xFF == ord('q'):
           #     break
            
            num=num+1
            
        else:
            break
    
    cap.release()
    out1.release()
    out2.release()
    #cv2.destroyAllWindows()

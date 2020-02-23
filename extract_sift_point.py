# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:38:27 2020

@author: sunhongbo
"""

import cv2

imgpath = './baozha2.jpg'
img = cv2.imread(imgpath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建SIFT对象
sift = cv2.xfeatures2d.SIFT_create()
keypoints, descriptor = sift.detectAndCompute(gray, None)

img = cv2.drawKeypoints(image=img, 
						outImage=img, 
						keypoints = keypoints, 
				        flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, 
						color = (0, 0, 255))


cv2.imshow('sift_jianzhu_01', img)

cv2.imwrite("image_sift_feature_point.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:56:09 2020

@author: sunhongbo
"""

import cv2
import numpy as np

img = cv2.imread("//Mac/Home/Desktop//baozha2.jpg", 0)
cv2.imwrite("canny.jpg", cv2.Canny(img, 60, 100))
cv2.imshow("canny", cv2.imread("canny.jpg"))
cv2.waitKey()

cv2.destroyAllWindows()
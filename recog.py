# -*- coding: utf-8 -*- 
""" 
Created on Tue Sep 26 23:15:39 2017 
 
@author: tina 
""" 
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
 
img = cv2.imread('line//line1.png') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
 
circles1 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1, 
600,param1=100,param2=30,minRadius=10,maxRadius=35) 
circles = circles1[0,:,:] 
circles = np.uint16(np.around(circles)) 

for i in circles[:]: 
    #圆的基本信息
    #坐标行列
    x=int(i[0])
    y=int(i[1])
    #半径
    r=int(i[2])
    #在原图用指定颜色标记出圆的位置
    roi = gray[y-r:y+r,x-r:x+r]
    cv2.circle(img,(x,y),r,(255,0,0),2) 
 #cv2.circle(img,(x,y),2,(255,0,255),2) 
 #cv2.rectangle(img,(i[0]-i[2],i[1]+i[2]),(i[0]+i[2],i[1]-i[2]),(255,255,0),1) 
 
print("圆心坐标",x,y) 
print("半径",r)
cv2.imshow("image",img)
cv2.imshow("roi",roi)
cv2.waitKey (0)  
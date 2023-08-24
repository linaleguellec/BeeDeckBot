# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:23:21 2023

@author: linal
"""

import numpy as np
import cv2

video_path = "D:/GitHub_BeeDeckBot/BeeDeckBot/videos_abeilles_brut/500_fps/cible_immobile/I1.MP4"

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(video_path)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))

# initializing subtractor
MOG2 = cv.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    maskMOG = MOG2.apply(frame)
    mask1 = cv.morphologyEx(maskMOG, cv.MORPH_OPEN, kernel)	# eleve les points blanc restats indésirables 
    _, mask2 = cv.threshold(mask1, 100, 255, cv2.THRESH_BINARY) 
    mask3 = cv.dilate(mask2,kernel,iterations = 5)
    contours, hierarchy = cv.findContours(mask3, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame, contours, -1, (0,255,255), 2)
    
    for cnt in contours:
      
        # Calculate and draw circle
        (x, y), radius = cv.minEnclosingCircle(cnt)
        x = int(x)
        y = int(y)
        radius = int(radius)
        cv.circle(frame, (x, y), radius, (0, 255, 0), 2)
        cv2.rectangle(frame, (x-radius, y - radius), (x+radius, y + radius), (0, 0, 255), 2)
            
    
    
    cv.imshow('mog', maskMOG)
    cv.imshow('1', mask1)
    cv.imshow('2', mask2)
    cv.imshow('3', mask3)
    cv.imshow('maskContours', frame)
    
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 10:17:38 2023

@author: linal
"""

import cv2 as cv
import numpy as np



def nothing(x):
    pass


# MOG2 
class Detector1(object):
    def __init__(self, DEBUG):
        self.kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)) #structure ellipse de 3 par 3
        self.MOG2 = cv.createBackgroundSubtractorMOG2()
        self.DEBUG=DEBUG
       

    def detect(self, frame):
        maskMOG = self.MOG2.apply(frame)
        mask1 = cv.morphologyEx(maskMOG, cv.MORPH_OPEN, self.kernel)	# eleve les points blanc restats indésirables 
        _, mask2 = cv.threshold(mask1, 100, 255, cv.THRESH_BINARY) 
        mask3 = cv.dilate(mask2, self.kernel,iterations = 5)
        contours, hierarchy = cv.findContours(mask3, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(frame, contours, -1, (0,255,255), 2)
        
        detections = []
        detections.append([0, 0 , 10, 50, 0])
        
        for cnt in contours:
          
            # Calculate and draw circle
            (x, y), radius = cv.minEnclosingCircle(cnt)
            x = int(x)
            y = int(y)
            radius = int(radius)
            cv.circle(frame, (x, y), 2, (0, 255, 0), 2)
            # cv.rectangle(frame, (x-radius, y - radius), (x+radius, y + radius), (0, 0, 255), 2)
            detections.append([x-radius, y - radius, x+radius , y + radius , 1])

            
            if self.DEBUG: 
                cv.imshow('mog', maskMOG)
                cv.imshow('1', mask1)
                cv.imshow('2', mask2)
                cv.imshow('3', mask3)
                cv.imshow('maskContours', frame)
                
        return (detections)
    
    
    
    
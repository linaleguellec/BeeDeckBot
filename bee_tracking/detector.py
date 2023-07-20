# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 10:17:38 2023

@author: linal
"""

import cv2 as cv
import numpy as np



def nothing(x):
    pass


class Detector1(object):
    def __init__(self, DEBUG):
        self.kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)) #structure ellipse de 3 par 3
        self.fgbg = cv.createBackgroundSubtractorMOG2()
        self.blob_radius_min = 3
        self.blob_radius_max = 10
        self.DEBUG=DEBUG
       

    def detect(self, current):
        #cropped=frame[(frame.shape[0]-1000):frame.shape[0],0:frame.shape[1]] 
        fgmask = self.fgbg.apply(current)
        
        _, threshold = cv.threshold(fgmask, 128, 255, cv.THRESH_BINARY) 
        
        fgmask = cv.morphologyEx(threshold, cv.MORPH_OPEN, self.kernel)
  
        contours, hierarchy = cv.findContours(fgmask, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)    
        frame_contours=current
        
        cv.drawContours(frame_contours, contours, -1, (0,0,255), 2)
        

        centers = []  # vector of object centroids in a frame
        detections = []
        detections.append([0, 0 , 10, 50, 1])
        epsilon = 20
        
        # Find centroid for each valid contours
        for cnt in contours:
            try:
                # Calculate and draw circle
                (x, y), radius = cv.minEnclosingCircle(cnt)
                centeroid = (int(x), int(y))
                radius = int(radius)
                if (radius > self.blob_radius_min and radius < self.blob_radius_max):
                    cv.circle(frame_contours, centeroid, radius, (0, 255, 0), 2)
                    b = np.array([[x], [y]])
                    centers.append(np.round(b))
                    detections.append([int(x - epsilon), int(y - epsilon) , int(x + epsilon) , int(y + epsilon) , 1])
                    
            except ZeroDivisionError:
                pass
            
            if self.DEBUG: 
                cv.imshow("frame_contours", frame_contours)
        #print (centers)

        return (detections ,frame_contours)
    
    
    
class Detector2(object):
    def __init__(self,bin_const_1,dil_const_1,bin_const_2,dil_const_2,DEBUG):
        self.blob_radius_thresh = 10
        
        self.DEBUG=DEBUG
        self.bin_const_1=bin_const_1
        self.bin_const_2=bin_const_2
        self.dil_const_1=dil_const_1
        self.dil_const_2=dil_const_2
        
        
        if self.DEBUG:
            cv.namedWindow("1gray", cv.WINDOW_NORMAL)
            cv.namedWindow("2binary", cv.WINDOW_NORMAL)
            cv.namedWindow("3addition", cv.WINDOW_NORMAL)
            cv.namedWindow("4gaussian", cv.WINDOW_NORMAL)
            cv.namedWindow("5dilate", cv.WINDOW_NORMAL)
            cv.namedWindow("6final", cv.WINDOW_NORMAL)
            cv.namedWindow("7dilate2", cv.WINDOW_NORMAL)
            cv.createTrackbar("binary1","2binary",bin_const_1,255,nothing)
            cv.createTrackbar("dilate iteration","5dilate",dil_const_1,20,nothing)
            cv.createTrackbar("binary final","6final",bin_const_2,254,nothing)
            cv.createTrackbar("dilate iteration 2","7dilate2",dil_const_2,20,nothing)
        print('Press ESC to exit cleanly')
      

    def detect(self, currentframe, previousframe):
        current=np.copy(currentframe)
        previous=np.copy(previousframe)
        previous_gray = cv.cvtColor(previous, cv.COLOR_BGR2GRAY)
        if self.DEBUG :
            previous_binary = cv.threshold(previous_gray,cv.getTrackbarPos("binary1", "2binary"),255,cv.THRESH_BINARY_INV)[1]
            gray = cv.cvtColor(current, cv.COLOR_BGR2GRAY) 
            binary = cv.threshold(gray,cv.getTrackbarPos("binary1", "2binary"),255,cv.THRESH_BINARY)[1]
            addition=cv.threshold(binary+previous_binary,127,255,cv.THRESH_BINARY_INV)[1]    
            gaussian = cv.GaussianBlur(addition, (21,21), 0)
            dilate = cv.dilate(gaussian, None, iterations=cv.getTrackbarPos("dilate iteration", "5dilate"))
            final=cv.threshold(dilate,cv.getTrackbarPos("binary final", "6final"),255,cv.THRESH_BINARY)[1]
            dilate2 = cv.dilate(final, None, iterations=cv.getTrackbarPos("dilate iteration 2", "7dilate2"))
        else :
            previous_binary = cv.threshold(previous_gray,65,255,cv.THRESH_BINARY_INV)[1]
            gray = cv.cvtColor(current, cv.COLOR_BGR2GRAY) 
            binary = cv.threshold(gray,self.bin_const_1,255,cv.THRESH_BINARY)[1]
            addition=cv.threshold(binary+previous_binary,127,255,cv.THRESH_BINARY_INV)[1]    
            gaussian = cv.GaussianBlur(addition, (21,21), 0)
            dilate = cv.dilate(gaussian, None, iterations=self.dil_const_1)
            final=cv.threshold(dilate,self.bin_const_2,255,cv.THRESH_BINARY)[1]
            dilate2 = cv.dilate(final, None, iterations=self.dil_const_2)
        
        contours_new, hierarchy = cv.findContours(dilate2,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        frame_contours=current
        cv.drawContours(frame_contours, contours_new, -1, (0,0,255), 2)
    
#    contours_final=[]
        centers = []
        rect = []

        for i in range(len(contours_new)):
#        if cv.contourArea(contours_new[i])>10.0:
#         #   if contours_new[i] in contours_old == True:
#            contours_final.append(contours_new[i])
            x,y,w,h = cv.boundingRect(contours_new[i])
            a=np.array([[x],[y],[w],[h]])
            rect.append(np.round(a))
            frame_contours = cv.rectangle(frame_contours,(x,y),(x+w,y+h),(255,0,0),2)
            b = np.array([[x+h/2], [y+w/2]])
            centers.append(np.round(b))
#    contours_old=contours_new
        
        if self.DEBUG: 
            cv.imshow("1gray", gray)
            cv.imshow("2binary", binary)
            cv.imshow("3addition", addition)
            cv.imshow("4gaussian", gaussian)
            cv.imshow("5dilate", dilate)
            cv.imshow("6final", final)
            cv.imshow("7dilate2", dilate2)
        return (centers,frame_contours,rect) 
    
    
    
    
class Detector3(object):
    def __init__(self,bin_const_1,dil_const_1,bin_const_2,dil_const_2,DEBUG):
        
        self.w_h_seuil = 1000  # surface seuil du rectangle qui entoure les contours  
        self.DEBUG=DEBUG

        
        
        if self.DEBUG:
            cv.namedWindow("gray", cv.WINDOW_NORMAL)
            cv.namedWindow("binary", cv.WINDOW_NORMAL)
            cv.namedWindow("binary_inv", cv.WINDOW_NORMAL)
            cv.namedWindow("erode", cv.WINDOW_NORMAL)
            cv.namedWindow("gaussian", cv.WINDOW_NORMAL)
            cv.namedWindow("dilate", cv.WINDOW_NORMAL)
            cv.namedWindow("binary2", cv.WINDOW_NORMAL)

        print('Press ESC to exit cleanly')
      

    def detect(self, currentframe):
        current=np.copy(currentframe)

        if self.DEBUG :

            gray = cv.cvtColor(current, cv.COLOR_BGR2GRAY) 
            binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
            binary_inv = cv.threshold(binary, 128, 255, cv.THRESH_BINARY_INV)[1]
            erode = cv.erode(binary_inv, None, iterations=1)  
            gaussian = cv.GaussianBlur(erode, (21,21), 0)
            dilate = cv.dilate(gaussian, None, iterations=5)
            binary2 = cv.threshold(dilate, 40, 255, cv.THRESH_BINARY)[1]

        else :
            gray = cv.cvtColor(current, cv.COLOR_BGR2GRAY) 
            binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
            binary_inv = cv.threshold(binary, 128, 255, cv.THRESH_BINARY_INV)[1]
            erode = cv.erode(binary_inv, None, iterations=1)  
            gaussian = cv.GaussianBlur(erode, (21,21), 0)
            dilate = cv.dilate(gaussian, None, iterations=5)
            binary2 = cv.threshold(dilate, 40, 255, cv.THRESH_BINARY)[1]
            
        
        contours_new, hierarchy = cv.findContours(binary2 ,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        frame_contours=current
        cv.drawContours(frame_contours, contours_new, -1, (0,0,255), 2)
    
        centers = []
        rect = []

        for i in range(len(contours_new)):

            x,y,w,h = cv.boundingRect(contours_new[i])
            
            if ( w*h < self.w_h_seuil) : 
                a=np.array([[x],[y],[w],[h]])
                rect.append(np.round(a))
                frame_contours = cv.rectangle(frame_contours,(x,y),(x+w,y+h),(255,0,0),2)
                b = np.array([[x+h/2], [y+w/2]])
                centers.append(np.round(b))
        
        if self.DEBUG: 
            cv.imshow("gray", gray)
            cv.imshow("binary", binary)
            cv.imshow("binary_inv", binary_inv)
            cv.imshow("erode", erode)
            cv.imshow("gaussian", gaussian)
            cv.imshow("dilate", dilate)
            cv.imshow("binary2", binary2)
            
        return (centers,frame_contours,rect) 





class Detector4(object):
    def __init__(self, DEBUG):
        
        self.w_h_seuil = 1000  # surface seuil du rectangle qui entoure les contours  
        self.DEBUG=DEBUG

        
        
        if self.DEBUG:
            cv.namedWindow("gray", cv.WINDOW_NORMAL)
            cv.namedWindow("binary", cv.WINDOW_NORMAL)
            cv.namedWindow("binary_inv", cv.WINDOW_NORMAL)
            cv.namedWindow("erode", cv.WINDOW_NORMAL)
            cv.namedWindow("gaussian", cv.WINDOW_NORMAL)
            cv.namedWindow("dilate", cv.WINDOW_NORMAL)
            cv.namedWindow("binary2", cv.WINDOW_NORMAL)

        print('Press ESC to exit cleanly')
      

    def detect(self, currentframe):
        current=np.copy(currentframe)

        if self.DEBUG :

            gray = cv.cvtColor(current, cv.COLOR_BGR2GRAY) 
            binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
            binary_inv = cv.threshold(binary, 128, 255, cv.THRESH_BINARY_INV)[1]
            erode = cv.erode(binary_inv, None, iterations=1)  
            gaussian = cv.GaussianBlur(erode, (21,21), 0)
            dilate = cv.dilate(gaussian, None, iterations=5)
            binary2 = cv.threshold(dilate, 40, 255, cv.THRESH_BINARY)[1]

        else :
            gray = cv.cvtColor(current, cv.COLOR_BGR2GRAY) 
            binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
            binary_inv = cv.threshold(binary, 128, 255, cv.THRESH_BINARY_INV)[1]
            erode = cv.erode(binary_inv, None, iterations=1)  
            gaussian = cv.GaussianBlur(erode, (21,21), 0)
            dilate = cv.dilate(gaussian, None, iterations=5)
            binary2 = cv.threshold(dilate, 40, 255, cv.THRESH_BINARY)[1]
            
        
        contours_new, hierarchy = cv.findContours(binary2 ,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        frame_contours=current
        cv.drawContours(frame_contours, contours_new, -1, (0,0,255), 2)
    
        centers = []
        rect = []
        detections = []

        for i in range(len(contours_new)):

            x,y,w,h = cv.boundingRect(contours_new[i])
            
            if ( w*h < self.w_h_seuil) : 
                a=np.array([[x],[y],[w],[h]])
                rect.append(np.round(a))
                frame_contours = cv.rectangle(frame_contours,(x,y),(x+w,y+h),(255,0,0),2)
                b = np.array([[x+h/2], [y+w/2]])
                centers.append(np.round(b))
                detections.append([x, y, x + w , y + h, 1])
        
        if self.DEBUG: 
            cv.imshow("gray", gray)
            cv.imshow("binary", binary)
            cv.imshow("binary_inv", binary_inv)
            cv.imshow("erode", erode)
            cv.imshow("gaussian", gaussian)
            cv.imshow("dilate", dilate)
            cv.imshow("binary2", binary2)
            
        return (detections, frame_contours) 
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 18:48:00 2023

@author: linal
"""
import cv2
import numpy as np
from detector import Detector1, Detector2, Detector3, Detector4


#Chemin vers le fichier vidéo
video_path = "D:/projet_beedeckbot/codes_python_v3/videos/video2.mp4"

num_detector = 4
#mode debug pour le détecteur 2, multi fenetre et reglage des paramètres
DEBUG=1

playVideo = True

#Créer un objet capture vidéo
cap = cv2.VideoCapture(video_path)

#Création de la fenetre de detection et prise 1ere image
cv2.namedWindow("detection", cv2.WINDOW_NORMAL)
ok, frame = cap.read()

if not ok:
    print('Failed to read video')
    exit()
    
    
# Select ROI
r = cv2.selectROI("detection",frame)
cv2.destroyWindow("detection")


# Crop image
cropped = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]


# creation detector 
if num_detector==1:
    MyDetector = Detector1()
    
elif num_detector==2:
    previous_frame=cropped
    MyDetector = Detector2(120,0,150,8,DEBUG)
    
elif num_detector==3:
    
    MyDetector = Detector3(120,0,150,8,DEBUG)
    
else : 
   
    MyDetector = Detector4(120,0,150,8,DEBUG)
    


while True:
    
    if playVideo:
        # Lire une nouvelle frame de la vidéo
        ret, frame = cap.read()
    
    
        # Vérifier si la lecture de la frame a réussi
        if not ret:
            break
        centers = []
        imgs = []
        rect = []
        cropped = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        
        
        if num_detector==1:
            centers,frame2 = MyDetector.detect(cropped)
        
        if num_detector==2:
            centers,frame2,rect = MyDetector.detect(cropped,previous_frame)
            #cv.imshow("bee", cropped)
            previous_frame=np.copy(cropped)    
            for i in range(len(centers)):
                imgs.append(cropped[int(rect[i][1]):int(rect[i][1]+rect[i][3]),int(rect[i][0]):int(rect[i][0]+rect[i][2])])
                
        if num_detector==3:
            centers,frame2,rect = MyDetector.detect(cropped)   
            for i in range(len(centers)):
                imgs.append(cropped[int(rect[i][1]):int(rect[i][1]+rect[i][3]),int(rect[i][0]):int(rect[i][0]+rect[i][2])])
                
        if num_detector==4:
            centers,frame2,rect = MyDetector.detect(cropped)   
            for i in range(len(centers)):
                imgs.append(cropped[int(rect[i][1]):int(rect[i][1]+rect[i][3]),int(rect[i][0]):int(rect[i][0]+rect[i][2])])
    
    
        cv2.imshow("detection",frame2) 
    
    k = cv2.waitKey(50);
    if k == 27: #ascii ESC
        break
    if k == 112: #ascii p
        playVideo = not playVideo
  
cap.release()
cv2.destroyAllWindows()
    


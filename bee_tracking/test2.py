# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 18:48:00 2023

@author: linal
"""
import cv2
import numpy as np
from detector import Detector4
import os
import random
from tracker import Tracker

# pour ne pas avoir un message d'erreur 
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# Chemin vers le fichier vidéo
video_path = "D:/projet_beedeckbot/codes_python_v3/videos/video2.mp4"

# mode debug 
DEBUG=0

playVideo = True

# Créer un objet capture vidéo
cap = cv2.VideoCapture(video_path)

# Création de la fenetre de detection et prise 1ere image
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
MyDetector = Detector4(DEBUG)
    
# creation du tracker    
tracker = Tracker()

# couleur au hasard pour encadrer chaque nouvelle abeille 
colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for j in range(10)]

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
        
        frame_tracker = current=np.copy(cropped)
        
        
        detections, frame_detection = MyDetector.detect(cropped)  
        
        tracker.update(cropped, detections)
        
        for track in tracker.tracks:
            bbox = track.bbox
            x1, y1, x2, y2 = bbox
            track_id = track.track_id

            cv2.rectangle(frame_tracker, (int(x1), int(y1)), (int(x2), int(y2)), (colors[track_id % len(colors)]), 3)

        
        cv2.imshow("detection",frame_detection) 
        cv2.imshow("tracker",frame_tracker) 
    
    k = cv2.waitKey(50);
    if k == 27: #ascii ESC
        break
    if k == 112: #ascii p
        playVideo = not playVideo
  
cap.release()
cv2.destroyAllWindows()
    


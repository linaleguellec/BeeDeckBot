# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:38:15 2023

@author: linal
"""

import cv2

# Variable globale pour enregistrer la position de la souris
X_separation = 10

def get_mouse_position(event, x, y, flags, param):
    global X_separation
    if event == cv2.EVENT_LBUTTONDOWN:
        X_separation = x
        print('lina')

        

# Chemin vers le fichier vidéo
video_path = "D:/GitHub_BeeDeckBot/BeeDeckBot/videos_abeilles_brut/500_fps/cible_immobile/I1.MP4"
cap = cv2.VideoCapture(video_path)

cv2.namedWindow("Video")
cv2.setMouseCallback("Video", get_mouse_position)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("Video", frame)
    
    key = cv2.waitKey(1)
    if key == 27:  # Touche ESC pour quitter
        break

cap.release()
cv2.destroyAllWindows()




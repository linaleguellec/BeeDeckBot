# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:51:51 2023

@author: Stagiaire
"""

"""

fonctionne le 30 juin 2023 

separe les images en 2 de la calibration
"""


import cv2
import numpy as np
from PIL import Image
import glob 




  

if __name__ == "__main__":
    
    
    chessboardSize = (25,18)
    frameSize = (1440,1080)

    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
    objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

    size_of_chessboard_squares_mm = 30
    objp = objp * size_of_chessboard_squares_mm


    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    
    
    dossier_images_entree = "C:/Users/Stagiaire/Desktop/CameraCalibration/images4"  # Chemin vers le dossier des images d'entrée
    images = glob.glob(f"{dossier_images_entree}/*.png")
    
    image = images[0]
    
    nom_image = image.split("\\")[-1].split(".")[0]
    img = cv2.imread(image, 1)
    #largeur, hauteur, cannaux = img.shape
    cv2.imshow('img', img)
    cv2.waitKey(0)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img', gray)
    cv2.waitKey(0)
    
    ret, corners = cv2.findChessboardCorners(gray, chessboardSize, None)
    
    # If found, add object points, image points (after refining them)
    if ret == True:

        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, chessboardSize, corners2, ret)
        
        cv2.imshow('img', img)
        cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    
    
    
    

        


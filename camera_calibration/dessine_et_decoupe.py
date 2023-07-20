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

from PIL import Image

import glob 

hauteur_coupure = None 


def click_event(event, x, y, flags, params):
    global hauteur_coupure
    if event == cv2.EVENT_LBUTTONDOWN:
        img_copy = img.copy()
        img2 = cv2.line(img_copy, (x, 0), (x, largeur), (0, 0, 255), 4)
        cv2.imshow('image', img2)
        hauteur_coupure = x

  
  

def decouper_image(hauteur_coupure):

    # Vérifier si l'emplacement de coupure est valide
    if hauteur_coupure <= 0 or hauteur_coupure >= hauteur:
        print("L'emplacement de coupure est invalide.")
        return

    # Couper l'image en deux parties
    partie_superieure = img[0:largeur, 0:hauteur_coupure ]
    partie_inferieure = img[0:largeur, hauteur_coupure:hauteur ]
    
    # Convertir les tableaux NumPy en objets Image
    partie_superieure = Image.fromarray(cv2.cvtColor(partie_superieure, cv2.COLOR_BGR2RGB))
    partie_inferieure = Image.fromarray(cv2.cvtColor(partie_inferieure, cv2.COLOR_BGR2RGB))

    # Enregistrer les deux images coupées
    #nom_image = image_path.split("/")[-1].split(".")[0]
    partie_superieure.save(f"{dossier_sortie_superieur}/{nom_image}_partie_superieure.jpg")
    partie_inferieure.save(f"{dossier_sortie_inferieur}/{nom_image}_partie_inferieure.jpg")

    print("Les images ont été découpées et enregistrées avec succès.")
    
    
    

if __name__ == "__main__":
    
    dossier_images_entree = "C:/Users/Stagiaire/Desktop/CameraCalibration/images_cali_bas"  # Chemin vers le dossier des images d'entrée
    dossier_sortie_superieur = "C:/Users/Stagiaire/Desktop/CameraCalibration/coupe/superieur"  # Chemin vers le dossier où enregistrer les images coupées
    dossier_sortie_inferieur = "C:/Users/Stagiaire/Desktop/CameraCalibration/coupe/inferieur"  # Chemin vers le dossier où enregistrer les images coupées
    
    images = glob.glob(f"{dossier_images_entree}/*.JPG")
    
    image = images[0]
    
    nom_image = image.split("\\")[-1].split(".")[0]
    img = cv2.imread(image, 1)
    largeur, hauteur, cannaux = img.shape
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    decouper_image(hauteur_coupure)
    cv2.destroyAllWindows()

    for image in images[1: len(images) ]:

        nom_image = image.split("\\")[-1].split(".")[0]
        img = cv2.imread(image, 1)
        largeur, hauteur, cannaux = img.shape
        cv2.imshow('image', img)
        decouper_image(hauteur_coupure)
        cv2.destroyAllWindows()
        
        
        


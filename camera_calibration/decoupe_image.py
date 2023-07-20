# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:02:10 2023

@author: Stagiaire
"""

from PIL import Image



def decouper_image_horizontal(image_path, hauteur_coupure, dossier_sortie):
    # Charger l'image
    image = Image.open(image_path)
    hauteur, largeur = image.size

    # Vérifier si l'emplacement de coupure est valide
    if hauteur_coupure <= 0 or hauteur_coupure >= hauteur:
        print("L'emplacement de coupure est invalide.")
        return

    # Couper l'image en deux parties
    partie_superieure = image.crop((0, 0, hauteur_coupure, largeur)) # partie gauche 
    partie_inferieure = image.crop((hauteur_coupure, 0, hauteur, largeur)) # partie droite 

    # Enregistrer les deux images coupées
    nom_image = image_path.split("/")[-1].split(".")[0]  # Extraire le nom de l'image sans extension
    partie_superieure.save(f"{dossier_sortie}/{nom_image}_partie_superieure.jpg")
    partie_inferieure.save(f"{dossier_sortie}/{nom_image}_partie_inferieure.jpg")

    print("Les images ont été découpées et enregistrées avec succès.")

# Exemple d'utilisation
image_path = "C:/Users/Stagiaire/Desktop/CameraCalibration/images4/image1.JPG"  # Chemin vers l'image d'entrée
hauteur_coupure = int(input("Entrez la hauteur de coupure : "))  # Hauteur de coupure choisie par l'utilisateur
dossier_sortie = "C:/Users/Stagiaire/Desktop/CameraCalibration/coupe"  # Chemin vers le dossier où enregistrer les images coupées

decouper_image_horizontal(image_path, hauteur_coupure, dossier_sortie)

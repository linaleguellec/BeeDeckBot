# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 10:24:18 2023

@author: Stagiaire


lit et affiche le contenu d'un fichier pkl 
"""

import pickle

# Chemin vers le fichier .pkl
fichier_pkl = "dist.pkl"

# Ouverture du fichier en mode lecture binaire
with open(fichier_pkl, "rb") as fichier:
    # Lecture du contenu du fichier .pkl
    contenu = pickle.load(fichier)

# Affichage du contenu
print(contenu)



# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:38:15 2023

@author: linal
"""

def supprimer_elements(lst, elements_a_supprimer):
    nouvelle_liste = [element for element in lst if element not in elements_a_supprimer]
    return nouvelle_liste

# Exemple d'utilisation
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elements_a_supprimer = [2, 4, 6, 8]
nouvelle_liste = supprimer_elements(ma_liste, elements_a_supprimer)
print("Nouvelle liste après suppression :", nouvelle_liste)


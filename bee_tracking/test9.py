
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 18:48:00 2023

@author: linal

animation 3D 

fonctionne le 24 juillet 

"""

#%% Section 0

import cv2
import numpy as np
from detector2 import Detector1
import os
import random
from tracker import Tracker
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from collections import Counter

#%% Section 1 : les fonctions 

# =============================================================================
# debut des fonctions 
# =============================================================================

def capture_plan(video_path) : 
    
    
    # mode debug 
    DEBUG=0

    playVideo = True
    
    cpt_frame = 0 
    
    results_tracker = []
    H = 0
    L = 0
    
    # Créer un objet capture vidéo
    cap = cv2.VideoCapture(video_path)
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_tot = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_tot/fps
    
    time = cpt_frame/fps
        
    
    # Création de la fenetre de detection et prise 1ere image
    cv2.namedWindow("detection", cv2.WINDOW_NORMAL)
    ok, frame = cap.read()
    

    cpt_frame = cpt_frame + 1 
    time = cpt_frame/fps
    #print(cpt_frame)
    
    if not ok:
        print('Failed to read video')
        exit()
        
        
    # Select ROI
    r = cv2.selectROI("detection",frame)
    cv2.destroyWindow("detection")
    
    
    # Crop image
    cropped = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    first_frame = cropped
    
    H, L, _ = first_frame.shape

    
    
    # creation detector 
    MyDetector = Detector1(DEBUG)
        
    # creation du tracker    
    tracker = Tracker()
    
    # couleur au hasard pour encadrer chaque nouvelle abeille 
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for j in range(10)]
    
    while True:
        
        if playVideo:
            # Lire une nouvelle frame de la vidéo
            ret, frame = cap.read()
            cpt_frame = cpt_frame + 1 
            time = cpt_frame/fps
            #print(cpt_frame)
        
        
            # Vérifier si la lecture de la frame a réussi
            if not ret:
                break
            
            
            
            
            cropped = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
            
            frame_tracker = current=np.copy(cropped)
            
            
            detections = MyDetector.detect(cropped)  
            
            tracker.update(cropped, detections)
            
            for track in tracker.tracks:
                bbox = track.bbox
                x1, y1, x2, y2 = bbox
                track_id = track.track_id
    
                cv2.rectangle(frame_tracker, (int(x1), int(y1)), (int(x2), int(y2)), (colors[track_id % len(colors)]), 3)
                
                cv2.circle(frame_tracker, (int(x1/2 + x2/2), int(y1/2 + y2/2))  , 3, (colors[track_id % len(colors)]), 3)
                
                cv2.circle(first_frame, (int(x1/2 + x2/2), int(y1/2 + y2/2))  , 3, (colors[track_id % len(colors)]), 1)
                
                results_tracker.append([cpt_frame, track_id , int(x1/2 + x2/2) , int(y1/2 + y2/2) ])
    
            
            cv2.imshow("tracker",frame_tracker) 
            cv2.imshow("trajectoire",first_frame)
            
        
        k = cv2.waitKey(50);
        if k == 27: #ascii ESC
            break
        if k == 112: #ascii p
            playVideo = not playVideo
            
            
    cap.release()
    cpt_frame = 0 
    cv2.destroyAllWindows() 

    return(results_tracker,L, H)       

      
            

    
    # mode debug 
    DEBUG=0

    playVideo = True
    
    cpt_frame = 0 
    
    results_tracker = []
    
    # Créer un objet capture vidéo
    cap = cv2.VideoCapture(video_path)
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_tot = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_tot/fps
    
    time = cpt_frame/fps
        
    
    # Création de la fenetre de detection et prise 1ere image
    cv2.namedWindow("detection", cv2.WINDOW_NORMAL)
    ok, frame = cap.read()
    cpt_frame = cpt_frame + 1 
    time = cpt_frame/fps
    #print(cpt_frame)
    
    if not ok:
        print('Failed to read video')
        exit()
        
        
    # Select ROI
    r = cv2.selectROI("detection",frame)
    cv2.destroyWindow("detection")
    
    
    # Crop image
    cropped = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    first_frame = cropped
    
    
    # creation detector 
    MyDetector = Detector1(DEBUG)
        
    # creation du tracker    
    tracker = Tracker()
    
    # couleur au hasard pour encadrer chaque nouvelle abeille 
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for j in range(10)]
    
    while True:
        
        if playVideo:
            # Lire une nouvelle frame de la vidéo
            ret, frame = cap.read()
            cpt_frame = cpt_frame + 1 
            time = cpt_frame/fps
            #print(cpt_frame)
        
        
            # Vérifier si la lecture de la frame a réussi
            if not ret:
                break
            
            
            
            
            cropped = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
            
            frame_tracker = current=np.copy(cropped)
            
            
            detections, frame_detection = MyDetector.detect(cropped)  
            
            tracker.update(cropped, detections)
            
            for track in tracker.tracks:
                bbox = track.bbox
                x1, y1, x2, y2 = bbox
                track_id = track.track_id
    
                cv2.rectangle(frame_tracker, (int(x1), int(y1)), (int(x2), int(y2)), (colors[track_id % len(colors)]), 3)
                
                cv2.circle(frame_tracker, (int(x1/2 + x2/2), int(y1/2 + y2/2))  , 3, (colors[track_id % len(colors)]), 3)
                
                cv2.circle(first_frame, (int(x1/2 + x2/2), int(y1/2 + y2/2))  , 3, (colors[track_id % len(colors)]), 3)
                
                results_tracker.append([cpt_frame, track_id , int(x1/2 + x2/2) , int(y1/2 + y2/2) ])
    
            
            cv2.imshow("detection",frame_detection) 
            cv2.imshow("tracker",frame_tracker) 
            cv2.imshow("trajectoire",first_frame)
            
            #print(results_tracker)
        
        k = cv2.waitKey(50);
        if k == 27: #ascii ESC
            break
        if k == 112: #ascii p
            playVideo = not playVideo
            
            
    cap.release()
    cpt_frame = 0 
    cv2.destroyAllWindows() 

    return(results_tracker, H, L)  



def animation_2D(X,Y) :         
    # Initialiser la figure et les axes
    fig, ax = plt.subplots()
    
    # Initialiser un objet ScatterPlot vide
    scatter = ax.scatter([], [])
    
    # Configurer les axes
    ax.set_xlim(0, 800)
    ax.set_ylim(0, 600)
    
    # Fonction d'animation pour mettre à jour les points progressivement
    def update(frame):
        if frame < len(X):
            # Ajouter un point à chaque frame
            scatter.set_offsets(np.vstack((X[:frame+1], Y[:frame+1])).T)
        return scatter,
    

    # Créer l'animation
    ani = animation.FuncAnimation(fig, update, frames=len(X)+1, interval=50, blit=True)
    
    # Afficher le graphique
    plt.show()
    
    k = cv2.waitKey(50);
    if k == 27: #ascii ESC
        return
    
def animation_3D(x,y,z) :         

    # Créer la figure et les axes 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlim(0, 550)
    ax.set_ylim(0, 450)
    ax.set_zlim(0, 913)

    # Tracer le nuage de points
    #ax.scatter(x, y, z)
    # ax.plot(x, y, z, color='green', linewidth=3)

    # Configurer les étiquettes des axes en bleu
    ax.set_xlabel('X [mm]', color='blue')
    ax.set_ylabel('Y [mm]', color='blue')
    ax.set_zlabel('Z [mm]', color='blue')


    def arrow3d(ax, x, y, z, dx, dy, dz, color, label):
        ax.quiver(x, y, z, dx, dy, dz, color=color, label=label, arrow_length_ratio=0.1)
    
    # Ajouter des flèches aux extrémités des axes
    arrow3d(ax, 0, 0, 0, 550, 0, 0, color='blue', label='$X$')
    arrow3d(ax, 0, 0, 0, 0, 450, 0, color='blue', label='$Y$')
    arrow3d(ax, 0, 0, 0, 0, 0, 913, color='blue', label='$Z$')
    
    # Tracer les faces du parallélépipède

    ax.plot([0, 550], [0, 0], [0, 0], color='black', linewidth=3)
    ax.plot([0, 0], [0, 450], [0, 0], color='black', linewidth=3)
    ax.plot([0, 0], [0, 0], [0, 913], color='black', linewidth=3)
    ax.plot([0, 0], [0, 450], [913, 913], color='black', linewidth=3)
    ax.plot([550, 550], [0, 450], [913, 913], color='black', linewidth=3)
    ax.plot([550, 550], [0, 450], [0, 0], color='black', linewidth=3)
    ax.plot([0, 550], [0, 0], [913, 913], color='black', linewidth=3)
    ax.plot([550, 550], [450, 450], [0, 913], color='black', linewidth=3)
    ax.plot([550, 550], [0, 0], [913, 0], color='black', linewidth=3)
    ax.plot([0, 550], [450, 450], [0, 0], color='black', linewidth=3)
    ax.plot([0, 550], [450, 450], [913, 913], color='black', linewidth=3)
    ax.plot([0, 0], [450, 450], [913, 0], color='black', linewidth=3)
    
    ax.plot([550, 550], [209, 237], [464, 464], color='black', linewidth=2)
    ax.plot([550, 550], [209, 237], [444, 444], color='black', linewidth=2)
    ax.plot([550, 550], [209, 209], [464, 444], color='black', linewidth=2)
    ax.plot([550, 550], [237, 237], [464, 444], color='black', linewidth=2)
    
    
    
    
    # Initialiser le nuage de points
    # points, = ax.plot([], [], [], 'bo')
    
    # Initialiser le nuage de points avec des points verts de petite taille
    points, = ax.plot([], [], [], 'go', markersize=3)
    
    # Fonction d'initialisation de l'animation
    def init():
        points.set_data([], [])
        points.set_3d_properties([])
        return points,
    
    # Fonction d'animation pour mettre à jour les points progressivement
    # def update(frame):
    #     if frame < len(x):
    #         # Mettre à jour les coordonnées des points jusqu'à la frame actuelle
    #         points.set_data(x[:frame+1], y[:frame+1])
    #         points.set_3d_properties(z[:frame+1])
    #     return points,
    
    # Créer une liste pour stocker les coordonnées des points tracés
    all_x = []
    all_y = []
    all_z = []
    
    # Fonction d'animation pour mettre à jour les points progressivement
    def update(frame):
        if frame < len(x):
            # Ajouter les coordonnées du point actuel à la liste
            all_x.append(x[frame])
            all_y.append(y[frame])
            all_z.append(z[frame])
            # Mettre à jour les coordonnées de tous les points jusqu'à la frame actuelle
            points.set_data(all_x, all_y)
            points.set_3d_properties(all_z)
        return points,
    
    
    # Désactiver l'interactivité de la souris
    plt.ioff()
    
    # Créer l'animation
    ani = animation.FuncAnimation(fig, update, frames=len(x)+1, init_func=init, interval=200, blit=True)
    
    # Afficher l'animation 3D
    plt.show()
    
    # Réactiver l'interactivité de la souris
    plt.ion()
    
    k = cv2.waitKey(50);
    if k == 27: #ascii ESC
        return


def graphique_3D(x,y,z) : 
    # Créer la figure et les axes 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlim(0, 550)
    ax.set_ylim(0, 450)
    ax.set_zlim(0, 913)

    # Tracer le nuage de points
    #ax.scatter(x, y, z)
    ax.plot(x, y, z, color='green', linewidth=3)

    # Configurer les étiquettes des axes en bleu
    ax.set_xlabel('X [mm]', color='blue')
    ax.set_ylabel('Y [mm]', color='blue')
    ax.set_zlabel('Z [mm]', color='blue')


    def arrow3d(ax, x, y, z, dx, dy, dz, color, label):
        ax.quiver(x, y, z, dx, dy, dz, color=color, label=label, arrow_length_ratio=0.1)
    
    # Ajouter des flèches aux extrémités des axes
    arrow3d(ax, 0, 0, 0, 550, 0, 0, color='blue', label='$X$')
    arrow3d(ax, 0, 0, 0, 0, 450, 0, color='blue', label='$Y$')
    arrow3d(ax, 0, 0, 0, 0, 0, 913, color='blue', label='$Z$')
    
    # Tracer les faces du parallélépipède

    ax.plot([0, 550], [0, 0], [0, 0], color='black', linewidth=3)
    ax.plot([0, 0], [0, 450], [0, 0], color='black', linewidth=3)
    ax.plot([0, 0], [0, 0], [0, 913], color='black', linewidth=3)
    ax.plot([0, 0], [0, 450], [913, 913], color='black', linewidth=3)
    ax.plot([550, 550], [0, 450], [913, 913], color='black', linewidth=3)
    ax.plot([550, 550], [0, 450], [0, 0], color='black', linewidth=3)
    ax.plot([0, 550], [0, 0], [913, 913], color='black', linewidth=3)
    ax.plot([550, 550], [450, 450], [0, 913], color='black', linewidth=3)
    ax.plot([550, 550], [0, 0], [913, 0], color='black', linewidth=3)
    ax.plot([0, 550], [450, 450], [0, 0], color='black', linewidth=3)
    ax.plot([0, 550], [450, 450], [913, 913], color='black', linewidth=3)
    ax.plot([0, 0], [450, 450], [913, 0], color='black', linewidth=3)
    
    ax.plot([550, 550], [209, 237], [464, 464], color='black', linewidth=2)
    ax.plot([550, 550], [209, 237], [444, 444], color='black', linewidth=2)
    ax.plot([550, 550], [209, 209], [464, 444], color='black', linewidth=2)
    ax.plot([550, 550], [237, 237], [464, 444], color='black', linewidth=2)
    
    
    
    # Afficher le graphique
    plt.show()


def graphique_2D(x,y):

    # Créer la figure et les axes
    fig, ax = plt.subplots()

    # Tracer le nuage de points
    ax.scatter(x, y)

    # Configurer les étiquettes des axes
    ax.set_xlabel('Axe X')
    ax.set_ylabel('Axe Y')

    # Afficher le graphique
    plt.show()
    
    
    
def deux_nombres_plus_frequents(lst):
    # Compter les occurrences des nombres dans la liste
    compteur = Counter(lst)
    
    # Trier les nombres en fonction de leurs occurrences (du plus fréquent au moins fréquent)
    nombres_tries = sorted(compteur, key=compteur.get, reverse=True)
    
    # Retourner les deux nombres les plus fréquents
    return nombres_tries[:2]
    

def supprimer_elements(lst, elements_a_supprimer):
    nouvelle_liste = [element for element in lst if element not in elements_a_supprimer]
    return nouvelle_liste


# =============================================================================
# fin des fonctions
# =============================================================================





#%% Section 2

# pour ne pas avoir un message d'erreur 
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


# Chemin vers le fichier vidéo
video_path = "D:/GitHub_BeeDeckBot/BeeDeckBot/videos_abeilles_brut/500_fps/cible_immobile/I1.MP4"

results_tracker, H, L  = capture_plan(video_path)
          

#%% Section 3


# creation d'une liste de résultats sans le pointen haur à gauche 
a_supprimer = []

k = len(results_tracker)

for i in range(0, k - 1) : 
        if (results_tracker[i][2] == 5 and results_tracker[i][3] == 25):
            a_supprimer.append(results_tracker[i])

results_tracker_court = supprimer_elements(results_tracker, a_supprimer)
a_supprimer = []


# recupération des id des abeilles 
id_list = []
k = len(results_tracker_court)
for i in range(0, k - 1) : 
    id_list.append(results_tracker_court[i][1])


indices_abeilles = deux_nombres_plus_frequents(id_list)


# création d'une liste avec que les results des 2 abeilles pertinantes 
l = len(indices_abeilles)
for i in range(0, k - 1) :
    for j in range (0, l -1) : 
        if (results_tracker[i][1] != indices_abeilles[j]):
            a_supprimer.append(results_tracker[i])
            
            
results_tracker_court = supprimer_elements(results_tracker_court, a_supprimer)
a_supprimer = []        
        


#%% Section 4

X = []
Y = []
Z = [] 
k = len(results_tracker_court)
xmoy1 = 0
xmoy2 = 0
c1 = 0 
c2 = 0 
a = 0 
for i in range(0, k - 1):
    if (results_tracker_court[i][1] == indices_abeilles[0] ) :
        c1 = c1 + 1 
        xmoy1 = xmoy1 + results_tracker_court[i][2]
        a = 1 
    

    if (results_tracker_court[i][1] == indices_abeilles[1] ) :
        c2 = c2 + 1 
        xmoy2 = xmoy2 + results_tracker_court[i][2]
        a = 2 
    
    if (a == 1):
        xmoy1 = xmoy1/c1
    if (a == 2): 
        xmoy2 = xmoy2/c2
    
    
    
if ( xmoy1 > xmoy2) : 
    for i in range(0, k - 1):
        # partie du haut 
        if (results_tracker_court[i][1] == indices_abeilles[0] ) :
            z = - results_tracker_court[i][2] + H 
            x = - results_tracker_court[i][3] + L 
            Z.append(z)
            X.append(x)
        
        # partie du bas 
        if (results_tracker_court[i][1] == indices_abeilles[1] ) :
            y = results_tracker_court[i][2]
            Y.append(y)

            
n = min(len(X), len(Y), len(Z))
X = X[:n] 
Y = Y[:n]
Z = Z[:n]  

# convertion pixels en mm hauteur de la boite réelle 
Xmm = []
Ymm = []
Zmm = [] 

h_boite = 913
l_boite = 550
L_boite = 450

for x in X : 
    x = (x/L)*l_boite
    Xmm.append(x)

for y in Y : 
    y = (y/H)*L_boite
    Ymm.append(y)
    

for z in Z : 
    z = (z/H)*h_boite
    Zmm.append(z)
    
    

#%% Section 5         
graphique_3D(Xmm, Ymm, Zmm)
    
    
# animation_3D(Xmm, Ymm, Zmm)
    




  
    
    
    
    
    
    

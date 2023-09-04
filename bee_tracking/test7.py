
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 18:48:00 2023

@author: linal

animation 3D 

fonctionne le 24 juillet 

"""
import cv2
import numpy as np
from detector2 import Detector1
import os
import random
from tracker import Tracker
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


###################### fonctions ##########################



def capture_plan(video_path) : 
    
    
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
            
            
            detections = MyDetector.detect(cropped)  
            
            tracker.update(cropped, detections)
            
            for track in tracker.tracks:
                bbox = track.bbox
                x1, y1, x2, y2 = bbox
                track_id = track.track_id
    
                cv2.rectangle(frame_tracker, (int(x1), int(y1)), (int(x2), int(y2)), (colors[track_id % len(colors)]), 3)
                
                cv2.circle(frame_tracker, (int(x1/2 + x2/2), int(y1/2 + y2/2))  , 3, (colors[track_id % len(colors)]), 3)
                
                cv2.circle(first_frame, (int(x1/2 + x2/2), int(y1/2 + y2/2))  , 3, (colors[track_id % len(colors)]), 3)
                
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

    return(results_tracker)       

      
            

    
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

    return(results_tracker)  



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
    
    # Initialiser le nuage de points
    points, = ax.plot([], [], [], 'bo')
    
    # Configurer les limites des axes
    ax.set_xlim(0, 800)
    ax.set_ylim(0, 800)
    ax.set_zlim(0, 800)
    
    # Fonction d'initialisation de l'animation
    def init():
        points.set_data([], [])
        points.set_3d_properties([])
        return points,
    
    # Fonction d'animation pour mettre à jour les points progressivement
    def update(frame):
        if frame < len(x):
            # Mettre à jour les coordonnées des points jusqu'à la frame actuelle
            points.set_data(x[:frame+1], y[:frame+1])
            points.set_3d_properties(z[:frame+1])
        return points,
    
    # Créer l'animation
    ani = animation.FuncAnimation(fig, update, frames=len(x)+1, init_func=init, interval=200, blit=True)
    
    # Afficher l'animation 3D
    plt.show()
    
    k = cv2.waitKey(50);
    if k == 27: #ascii ESC
        return


def graphique_3D(x,y,z) : 
    # Créer la figure et les axes 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # ax.set_xlim(0, 800)
    # ax.set_ylim(0, -800)
    # ax.set_zlim(0, 800)

    # Tracer le nuage de points
    ax.scatter(x, y, z)

    # Configurer les étiquettes des axes
    ax.set_xlabel('Axe X')
    ax.set_ylabel('Axe Y')
    ax.set_zlabel('Axe Z')

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
    
    
    

    
###################### fin fonctions ##########################



# pour ne pas avoir un message d'erreur 
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


# Chemin vers le fichier vidéo
video_path = "D:/GitHub_BeeDeckBot/BeeDeckBot/videos_abeilles_brut/500_fps/cible_immobile/I1.MP4"

results_tracker_x_z = capture_plan(video_path)
results_tracker_x_y = capture_plan(video_path)

            
X = []
Y = []
Z = []


k = min( len(results_tracker_x_y), len(results_tracker_x_z) )

for i in range(0, k - 1) : 
    x1 = results_tracker_x_z[i][2]
    y1 = results_tracker_x_z[i][3]
    x2 = results_tracker_x_y[i][2]
    X.append(y1)
    Y.append(x2)
    Z.append(x1)
    


X = X*2
Y = Y*2
Z = Z*2

graphique_3D(X, Y, Z)
  
    
    
    
    
    
    
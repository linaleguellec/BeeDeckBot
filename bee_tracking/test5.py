import cv2

# Chemin vers le fichier vidéo
video_path = "D:/projet_beedeckbot/codes_python_v3/videos/video2.mp4"

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

hauteur, largeur, canaux = frame.shape
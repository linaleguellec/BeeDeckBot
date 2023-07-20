"""

dessine une ligne horizontale quand on clique sur la souris et retourne les coordonné de clique 
"""


import cv2



def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        img_copy = img.copy()
        print(x, ' ', y)
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #img2 = cv2.putText(img, str(x) + ',' + str(y), (x, y), font, 1, (255, 0, 0), 2)
        img2 = cv2.line(img_copy, (x, 0), (x, largeur), (0, 0, 255), 4)
        cv2.imshow('image', img2)
        

if __name__ == "__main__":
    img = cv2.imread('sudoku.png', 1)
    hauteur, largeur, cannaux = img.shape
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




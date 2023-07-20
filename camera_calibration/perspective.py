"""
corrige la perspective

input : image avec les coordonnés de 4 coin a redresser et 
les coordonne des 4 coin de limage 
"""


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('sudoku.png')
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols,ch = img.shape
pts1 = np.float32([[66,76],[411,60],[32,431],[437,434]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()





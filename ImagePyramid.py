import cv2
import numpy as np

img = cv2.imread('lena.jpg')
#lr1 = cv2.pyrDown(img)
#lr2 = cv2.pyrDown(lr1)
#hr1 = cv2.pyrUp(lr2)
#cv2.imshow('Original Image', img)
#cv2.imshow('Lower Resolution Image', lr1)
#cv2.imshow('Lower Resolution Image 2', lr2)
#cv2.imshow('Higher Resolution Image', hr1)

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    ##cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_expanded)
    cv2.imshow(str(i), laplacian)

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

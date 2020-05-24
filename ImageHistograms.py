import numpy as np
import cv2

from matplotlib import pyplot as plt

#img = np.zeros((200, 200), np.uint8)
img = cv2.imread('lena.jpg', -1)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
#b, g, r = cv2.split(img)

#cv2.imshow('img', img)
#cv2.imshow('b', b)
#cv2.imshow('g', g)
#cv2.imshow('r', r)

#lt.hist(img.ravel(), 256, [0, 256])
#plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
#plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

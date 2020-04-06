import cv2
import numpy as np

img = cv2.imread('room.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)

layer = gp[6]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(6, 0, -1):
    gaussinan_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussinan_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow('Orginal Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
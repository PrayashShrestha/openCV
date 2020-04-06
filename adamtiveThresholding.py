import cv2
import numpy

img = cv2.imread('room.jpg', 0)
img = cv2.resize(img,None,fx=0.4, fy=0.4, interpolation = cv2.INTER_LINEAR)
#static thresholding
_, th = cv2.threshold(img, 70, 266, cv2.THRESH_BINARY)

#adaptive Thersholding
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 4)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 4)

cv2.imshow('img', img)
cv2.imshow('binary', th)
cv2.imshow('Gaussian', th1)
cv2.imshow('Mean', th2)

cv2.waitKey(0)
cv2.destroyAllWindows()

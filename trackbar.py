import cv2
import numpy as np

#define a function
def fun(x):
    print(x)

#create a window 
img = np.zeros((440,550,3),np.uint8) # a black window is created
#setting a name for the  window
cv2.namedWindow('frame')

#creating trackbar
cv2.createTrackbar('B', 'frame', 0, 255,  fun)
cv2.createTrackbar('G', 'frame', 0, 255,  fun)
cv2.createTrackbar('R', 'frame', 0, 255,  fun)
switch = '0 : OFF\n 1: ON'
cv2.createTrackbar(switch, 'frame', 0, 1, fun)

while(1):
    cv2.imshow('frame', img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

#taskbar position return
    b = cv2.getTrackbarPos('B', 'frame')
    g = cv2.getTrackbarPos('G', 'frame')
    r = cv2.getTrackbarPos('R', 'frame')
    s = cv2.getTrackbarPos(switch, 'frame')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.imshow('frame', img)
cv2.destroyAllWindows()
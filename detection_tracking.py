import cv2
import numpy as np

while (1):
    frame = cv2.imread('download.jfif')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_b = np.array([110, 50, 50])
    u_b = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, l_b, u_b)#here a mask variable contains lower and upper  range value to mask in the given image  
    res = cv2.bitwise_and(frame, frame, mask = mask)
    #here in bitwise and operation first src1 and src2 is iterated with
    #the mask value to get the color of given range and then the 
    #src1 and src 2 is ANDed

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(1)
    if key == 27 :
        break
    
cv2.destroyAllWindows()
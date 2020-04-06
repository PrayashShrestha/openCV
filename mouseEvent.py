import cv2
import numpy as np


#define a function for the mouse event 
def mouse_func(event, x, y, flages, param):
    #event to get the coordinate 
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',' ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ',' +str(y)
        cv2.putText(img, strXY, (x,y),font, 1, (255,255,0), 2)
        cv2.imshow('image', img)

    #event set for color channel
    if event == cv2.EVENT_RBUTTONDOWN:
        #set BGR color values in variable B-0, G-1, R-2
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue)+ ','+str(green)+ ','+str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (255,255,0), 2)
        cv2.imshow('image', img)


#set a dark  window frame
#img = np.zeros((512,512,3),np.uint8) 
img = cv2.imread('room.jpg', 1)
print(img)
cv2.imshow('image', img)
cv2.setMouseCallback('image', mouse_func)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
#to get the list of the events
events = [i for i in dir(cv2) if 'Event' in i]
print(events)'''
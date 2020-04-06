import cv2
import numpy as np

def fun(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
        points.append((x, y))#points stored to the list in the for of tuples

        #line should be made only when list has more than two points
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 255, 0), 3) #connects last and second last points
        cv2.imshow('frame', img)



img = cv2.imread('room.jpg', 1)
cv2.imshow('frame', img)
#this list is created so as to store the coordintes of the point where it was clicked
points = []
cv2.setMouseCallback('frame', fun)
cv2.waitKey(0)
cv2.destroyAllWindows()
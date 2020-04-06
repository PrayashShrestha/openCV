import cv2
import numpy as np

def fun():
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('TrackBar')
#Creating trackbar to set the Lower and Higher Limit of HSV
cv2.createTrackbar('LH', "TrackBar", 0, 255, fun)
cv2.createTrackbar('LS', "TrackBar", 0, 255, fun)
cv2.createTrackbar('LV', "TrackBar", 0, 255, fun)
cv2.createTrackbar('HH', "TrackBar", 255, 255, fun)
cv2.createTrackbar('HS', "TrackBar", 255, 255, fun)
cv2.createTrackbar('HV', "TrackBar", 255, 255, fun)

while True:
    #frame = cv2.imread('download.jfif') # its from image
    _, frame = cap.read() #its for live video
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #getting trackbar positions
    #Lower HSV
    l_h = cv2.getTrackbarPos("LH", "TrackBar")
    l_s = cv2.getTrackbarPos("LS", "TrackBar")
    l_v = cv2.getTrackbarPos("LV", "TrackBar")
    #Higher HSV
    h_h = cv2.getTrackbarPos("HH", "TrackBar")
    h_s = cv2.getTrackbarPos("HS", "TrackBar")
    h_v = cv2.getTrackbarPos("HV", "TrackBar")

    l_b = np.array([l_h, l_s, l_v])#Lower bound for image
    u_b = np.array([h_h, h_s, h_v])#upper bound for image

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', res)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('download.jfif',0)

_, mask = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
kernal = np.ones((3,3), np.uint8) #forms a white 3*3 square
dialation = cv2.dilate(mask, kernal, iterations=1)#works at main forground part
erosion = cv2.erode(mask, kernal, iterations=1)#works at the edge of the foreground part
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)#erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)#dialation followed by erotion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)#dialation - erosion
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)#mask - opening

titles = ['image', 'mask', 'dialation', 'erosion', 'opening', 'closing', 'mg','th']
images = [img, mask, dialation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

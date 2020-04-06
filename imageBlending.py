import numpy as np
import cv2

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

# print(apple.shape)
# print(orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

#image blending using pyramid
#steps:
'''
1. Load the Images
2. Find the gaussian Pyramids foe the images -> after gaussian process highest resolution is in starting index
3. From gaussian Pyramids, find the Laplacian Pyramids -> after lalplacian process lowest resolution is in starting index
4. Now join the left half and right half of the of both images  in each levels of laplacian pyramids -> adding of images occours from the starting index of the laplacian
    method i.e addition of images starts from the lowest resolution of images and  these are set in an array having lowest resolution images at starting addresses
5. Finally from this joint image pyramids, reconstruct the orginal image -> pyrUp the lowest index of joint image and add it up with the index at each iteration : and this image is again pyrUp and anded
'''
#generate gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#generate gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#generate laplacian pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

#generate laplacian pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)

#adding the images left of apple and right of orange
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap, in zip(lp_apple, lp_orange):
    n +=1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

#now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow('apple_orange', apple_orange)
cv2.imshow('apple_orange_reconstruct', apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
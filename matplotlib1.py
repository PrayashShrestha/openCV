import cv2
from matplotlib import pyplot as plt 
import numpy  

img = cv2.imread('download.jfif', 0)

_, th = cv2.threshold(img,30, 255, cv2.THRESH_BINARY)
_, th1 = cv2.threshold(img,30, 255, cv2.THRESH_BINARY_INV)
_, th2 = cv2.threshold(img,30, 255, cv2.THRESH_TOZERO)
_, th3 = cv2.threshold(img,30, 255, cv2.THRESH_TOZERO_INV)
_, th4 = cv2.threshold(img,30, 255, cv2.THRESH_TRUNC)

titles = ['Orginal', 'Binary', 'Binary_Inv', 'ToZero', 'ToZero_Inv', 'Trunc']
images = [img, th, th1, th2, th3, th4]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    #removes axis
    plt.xticks([])
    plt.yticks([]) 

plt.show()

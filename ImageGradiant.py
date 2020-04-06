import numpy as np
import cv2
from matplotlib import pyplot as  plt

img = cv2.imread('room.jpg',0)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=1)
#lab is in 64bit so converting it into 8bit uint
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=1)#affects to y axis
sobelY = cv2.Sobel(img, cv2.CV_64F,0, 1, ksize=1)#affects to x axis

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_and(sobelX, sobelY)
canny =cv2.Canny(img, 100, 200)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombined, canny]
for i in  range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
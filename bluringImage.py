import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images 1.jfif')
#matplotlib reads image in RGB format so converting it to that format
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#for filter2D  we should have size of kernal as 
# k= [ones matrix]*(1/(width * height of the kernal))
kernal = np.ones((5,5), np.float32)/25 
dst = cv2.filter2D(img, -1, kernal)

#Bluring Algorithms
blur = cv2.blur(img, (3,3))#equal filter coefficents
gblur = cv2.GaussianBlur(img, (5,5), 0)#variable filter coefficients
median = cv2.medianBlur(img, 3) #kernel should be odd and suitable for salt-peeper noise imaages
bilateralFilter = cv2.bilateralFilter(median, 9, 75, 75) #preserves the edges 

titles = ['orginal', '2D Convolution', 'Blur', 'GaussianBlur', 'Median','Bilateral']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

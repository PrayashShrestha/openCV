import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

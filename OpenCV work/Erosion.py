import cv2
import numpy as np

img = cv2.imread('photos/10.jpg')
img=cv2.resize(img,(500,500))
kernel = np.ones((10, 6), np.uint8)

# Using erode method
img_eroded = cv2.erode(img, kernel)

cv2.imshow('image', img_eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

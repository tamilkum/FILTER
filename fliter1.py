import cv2
import matplotlib.pyplot as plt
im1 = cv2.imread('efg.jpg')
d1 = cv2.GaussianBlur(im1,(75,75),cv2.BORDER_DEFAULT)
plt.imshow(d1)
plt.show()
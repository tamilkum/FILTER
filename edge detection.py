import cv2
import matplotlib.pyplot as plt
im1 = cv2.imread('efg.jpg')
edges = cv2.Canny(im1,100,300)
plt.imshow(edges)
plt.show()
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('family1.jpg')
img_resized = cv2.resize(img, (640,480))
img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

plt.subplot(1,2,1)
plt.imshow(img_resized)
plt.subplot(1,2,2)
plt.imshow(img_gray)
plt.show()
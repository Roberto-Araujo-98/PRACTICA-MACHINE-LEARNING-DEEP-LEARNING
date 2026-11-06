import cv2
img = cv2.imread('family1.jpg')
img_resized = cv2.resize(img, (640,480))
img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
cv2.imshow('cambio de tamaño', img_gray     )
cv2.waitKey(0)
cv2.destroyAllWindows()
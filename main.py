import cv2 # This is the essential first step to access all OpenCV functionalities.

img = cv2.imread("assets/cat.jpg", 1) 
img = cv2.resize(img, (0,0), fx=1, fy=1)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('cat_pic.jpg', img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



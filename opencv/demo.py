import cv2
image=cv2.imread('hello.jpg',1)
cv2.imshow('image',image)
cv2.waitKey(10000)
cv2.imwrite('hello.png',image)
cv2.destroyAllWindows()
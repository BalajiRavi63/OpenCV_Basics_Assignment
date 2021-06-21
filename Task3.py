import cv2
import imutils
img=cv2.imread("pic1.jpg")
img_mod=imutils.translate(img, 50, -100)
img_show1=cv2.imshow("Original Image", img)
img_show=cv2.imshow("Modified Image", img_mod)
cv2.waitKey(0)

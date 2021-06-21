import cv2
import numpy
import imutils

#img read 
img=cv2.imread("pic1.jpg")



#eye_ROI
eye = img[154:214, 185:235]
img[100:160, 10:60] = eye



#image show
imgshow=cv2.imshow("Image", img)
cv2.waitKey(0)

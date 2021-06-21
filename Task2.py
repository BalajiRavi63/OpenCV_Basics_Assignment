import cv2
import imutils
img=cv2.imread("pic1.jpg")
output = img.copy()
circle_img = cv2.circle(img,(220,198), 178, (0,0,255), 2) & cv2.putText(output, "Thinking Man", (395, 348),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow ("circle", circle_img )
cv2.waitKey(0)



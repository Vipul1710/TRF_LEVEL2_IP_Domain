import cv2
import numpy as np

img = cv2.imread('D:/TRF IP TASK/erosion.png')

kernel = np.ones((5,5),np.uint8)  # Here we have define a kernal of size (5,5) which will iterate all over the image

erosion = cv2.erode(img,kernel,iterations = 1)   #Here erosion is perform

dilation = cv2.dilate(img,kernel,iterations = 1)  #Here dilation is perform

cv2.imshow("original",cv2.resize(img,(400,600)))

cv2.imshow("erosion",cv2.resize(erosion,(400,600)))

cv2.imshow("dilation",cv2.resize(dilation,(400,600)))
#----------------------------------------------------


img1 = cv2.imread('D:/TRF IP TASK/opening.png')

img2 = cv2.imread('D:/TRF IP TASK/closing.png')

opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)  #Here opening is perform

closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)  #Here closing is perform

cv2.imshow("original opening",cv2.resize(img1,(400,600)))

cv2.imshow("original closing",cv2.resize(img2,(400,600)))

cv2.imshow("opening",cv2.resize(opening,(400,600)))

cv2.imshow("closing",cv2.resize(closing,(400,600)))

cv2.waitKey(0)
cv2.destroyAllWindows()
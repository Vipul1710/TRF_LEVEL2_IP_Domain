import cv2

img1 = cv2.imread('E:/TRF THEORY/IP/text.jpg')

img1=cv2.resize(img1,(500,700))

img2 = cv2.imread('E:/TRF THEORY/IP/download.jpg')

img2=cv2.resize(img2,(500,700))

dst = cv2.addWeighted(img1,0.4,img2,0.6,0) #Use to blend the image
#(first image , weight of first image , second image , weight of second image , alpha value )

cv2.imshow('dst',dst)

cv2.waitKey(0) #These function wait tell any key is press

cv2.destroyAllWindows() #This function destroies the windosws that are created
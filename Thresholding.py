import cv2
import numpy as np


text1=cv2.imread('E:/TRF THEORY/IP/text.jpg',3)    # Reads image

gray1=cv2.cvtColor(text1,cv2.COLOR_BGR2GRAY)    #Converts from BGR to gray

#Note : - image needed for thresholding should be in grayscale

#cv2.thresholding means if pixel value is greater than threshold it is assign to one value for eg whilte and if it
#is less than it is assign black

ret,thresh1=cv2.threshold(gray1,160,255,cv2.THRESH_BINARY) #Applying binary method

#(imagenamae , threshold value which is 160 in these case , max value i.e value given after pixel is greater than threshold ,
# Thresholding method )
#pixel>threshold == black
#pixel<threshold == white


ret,thresh2=cv2.threshold(gray1,133,255,cv2.THRESH_BINARY_INV)  #applying binary invet method

#(imagenamae , threshold value which is 133 in these case , max value i.e value given after pixel is greater than threshold ,
# Thresholding method )
#pixel>threshold == white
#pixel<threshold == black



titles = ['Original Image','BINARY','BINARY_INV']

images = [text1, thresh1, thresh2]
for i in range(3):
    cv2.imshow(titles[i],images[i])


gray1 = cv2.imread('E:/TRF THEORY/IP/text.jpg',0)
#gray1 = cv2.medianBlur(img,5)  # to make image blur

gaus=cv2.adaptiveThreshold(gray1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
#115 is block size,1 is constant,gaussian is adaptive process and threh binary is method


mean=cv2.adaptiveThreshold(gray1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,115,1)


titles = ['original Adaptive image','Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [gray1, gaus, mean]

for i in range(3):
    cv2.imshow(titles[i],images[i])


cv2.waitKey(0)                              # waiting till we press and key waitkey is 0 mwans we can press any key to end
cv2.destroyAllWindows()

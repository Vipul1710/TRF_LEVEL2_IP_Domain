import cv2
import numpy as np

img=cv2.imread('E:/TRF THEORY/IP/download.jpg',3)    # reading image

cv2.imshow('imag',img)                               # printing image

res=cv2.resize(img,(500,500))                     # resizing image

cv2.imshow('img',res)

gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)   # converting from color to gray scale
#(imagename , method of conversion)

hsv=cv2.cvtColor(res,cv2.COLOR_BGR2HSV)     # converting from color to hsv

cv2.imshow('img',res)

print(img.shape)                            # print the shape of the original image and no. of channel

print(res.shape)                            # print the shape of the resized image and no. of channel

cv2.imshow('gray',gray)                     # in '' there is image name and after , it is variable in which image is shown

cv2.imshow('hsv',hsv)

cv2.waitKey(0)                              # waiting till we press and key
cv2.destroyAllWindows()
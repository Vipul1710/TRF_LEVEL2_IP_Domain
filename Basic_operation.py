import cv2

image=cv2.imread("E:/TRF THEORY/IP/download.jpg") #Here we read images from specified folder
#(Path of image , specifies the way image should be read)

print("Shape of original image",image.shape)
#(imagename.shape is use to print shape of image)
# ( .shape first prints height , width , no. of channel )

image=cv2.resize(image,(500,700)) #These function resizes the image to specific size
#(imagename , (width,height))

print("Shape of resized image",image.shape)

cv2.imshow("imgK",image) #These function displays the image on screen
#(windowname , imagename)

cv2.imwrite("E:/TRF THEORY/IP/image.jpg",image) #These function save the image to given path
                                                # by the name mention in that path

cv2.waitKey(0) #These function wait tell any key is press

cv2.destroyAllWindows() #This function destroies the windosws that are created
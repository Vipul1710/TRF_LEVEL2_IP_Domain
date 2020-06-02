import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5) #Use to draw line
#(imagename , starting point ,ending point , color , thickness)

img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3) #Use to draw rectangle
#(imagename , top left corner , bottom right corner , color , thickness)

img = cv2.circle(img,(447,63), 63, (0,0,255), 5)  #Use to draw circle
#(imagename , center coordinates ,radius ,color , thickness )
#thickness == -1 or any negative number gives solid ellipse

img = cv2.ellipse(img,(256,256),(100,50),10,0,270,(15,255,255),-1) #Use to draw the ellipse on the screen
#(Imagename , senter location , (majoraxis,minoraxis) ,angle of rotation ,startAngle , endAngle , color , thickness)
#thickness == -1 or any negative number gives solid ellipse

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,450), font, 4,(255,255,255),5,cv2.LINE_AA) #Prints text on the screen
#(imagename , text to be written , coordinates of text , font type , font size , color scheme , thickness ,line type

cv2.imshow("img",img) #These function displays the image on screen

cv2.waitKey(0) #These function wait tell any key is press

cv2.destroyAllWindows() #This function destroies the windosws that are created
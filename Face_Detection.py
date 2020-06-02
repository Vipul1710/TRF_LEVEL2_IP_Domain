import cv2
import numpy as np

# Here we give path to cascade file
face_cascade =cv2.CascadeClassifier('C:/Users/DELL/PycharmProjects/TRF_Level2/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade =cv2.CascadeClassifier('C:/Users/DELL/PycharmProjects/TRF_Level2/venv/Lib/site-packages/cv2/data/haarcascade_eye.xml')
cap=cv2.VideoCapture(0)
while True:
    rat,frame=cap.read(0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,4)  #If face is found in the image then it returns the coordinates of it

    for (x,y,w,h) in faces:   #Then we run for loop over the list
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)        #Then we draw the rectangle
        roi_gray = gray[y:y + h, x:x + w]                       # Then with the coordinates of face we cut that image an we pass it
                                                                # eye cascade file
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)         #If eyes are found then it returs eye coordinate
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  #Then we draw the rectangle

    cv2.imshow('img',frame)

    k=cv2.waitKey(1)
    if k==32:
        break
cap.release()
cap.destroyAllWindows()
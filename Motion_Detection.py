import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # here 0 is indicating to play default camera if we attch external camera we should write 1
ret, frame1 = cap.read(0)
old = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)  # Here we store first frame for reference

while True:

    ret, frame = cap.read(0)  # here also 0 is use for same
    new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #Here the current frame is capture
    diff = cv2.absdiff(new, old)        # Here we take difference between the old frame and new frame
    cv2.imshow('frame12', diff)         # Here we print the differenece between both which is in the form of image

    old = new                           #here we assign new frame to old frame

    if cv2.waitKey(1) == 32:           # Here the web cam will stop working only when spacebar is press
        break
cap.release()

cv2.destroyAllWindows()
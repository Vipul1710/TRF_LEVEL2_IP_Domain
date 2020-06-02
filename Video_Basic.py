
import cv2

cap = cv2.VideoCapture(0)  # Here we create a variable for video capture

while(True):
    # Capture frame-by-frame

    ret, frame = cap.read()  #cap captures frame  by frame and it get store in frame , if there is any hardware issue
                             # then value of ret becomes false or else it is true

    # Our operations on the frame come here
    cv2.imshow("original",frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('gray',gray)    # Here we convert BGR to HSV

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the resulting frame
    cv2.imshow('hsv', hsv)     # Here we convert BGR to HSV

    if cv2.waitKey(1) & 0xFF == ord('q'): # web cam stops working when q is press
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
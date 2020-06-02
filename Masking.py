import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # Here we create video capture variable


def nothing(x):
    pass


def colormask():
    cv2.namedWindow("Masking", 1)        # here we create a windows

    # set trackbar
    bh = 'blue high'         #Here we declare variable by giving them name
    bl = 'blue low'
    gh = 'green high'
    gl = 'green low'
    rh = 'red high'
    rl = 'red low'

    # set range
    cv2.createTrackbar(bl, "Masking", 0, 255, nothing)    # These function create trackbar
    cv2.createTrackbar(gl, "Masking", 0, 255, nothing)    #(variable name , window name , lower value , higher value ,callback function)
    cv2.createTrackbar(rl, "Masking", 0, 255, nothing)
    cv2.createTrackbar(bh, "Masking", 0, 255, nothing)
    cv2.createTrackbar(gh, "Masking", 0, 255, nothing)
    cv2.createTrackbar(rh, "Masking", 0, 255, nothing)

    while True:
        ret, frame = cap.read(0)       # Here we capture the frame from web cam

        # convert rgb to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   #here we convert frame to hsv

        btl = cv2.getTrackbarPos(bl, "Masking")    #These function give us the position of trackbar
        gtl = cv2.getTrackbarPos(gl, "Masking")
        rtl = cv2.getTrackbarPos(rl, "Masking")
        bth = cv2.getTrackbarPos(bh, "Masking")
        gth = cv2.getTrackbarPos(gh, "Masking")
        rth = cv2.getTrackbarPos(rh, "Masking")

        rgbl = np.array([btl, gtl, rtl], np.uint8)   #Then we create array with lower value
        rgbh = np.array([bth, gth, rth], np.uint8)   #Then we create array with higher value

        # Threshold the HSV image to get only orange colors
        mask = cv2.inRange(hsv, rgbl, rgbh)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Mask", mask)
        cv2.imshow("Original Mask",res)
        cv2.imshow("Original", frame)

        k = cv2.waitKey(1)
        if k == 32:
            break


colormask()

cap.release()
cv2.destroyAllWindows()
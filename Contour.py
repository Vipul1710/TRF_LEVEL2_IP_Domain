import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read(0)
    img_copy = frame.copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.Canny(frame, 100, 115)
    contours, hierarchy = cv2.findContours(frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    print(contours)
    for contour in contours:
        image = cv2.drawContours(img_copy, contour, -1, (0, 255, 0), 3)
    cv2.imshow('frame', image)
    cv2.imshow('Canny', frame)

    k = cv2.waitKey(1)
    if k == 32:
        break
cap.release()
cv2.destroyAllWindows()
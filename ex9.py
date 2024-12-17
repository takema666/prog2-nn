import sys
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened:
    sys.exit('No camera available')

while True:
    result,frame = cap.read()
    if frame is None:
        print('no frame')
        break

    frame = cv.flip(frame,1)
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.imshow('camera',frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

cap.release()
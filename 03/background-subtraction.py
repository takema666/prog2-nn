import sys
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened:
    sys.exit('No camera available')

background = None

while True:
    result,frame = cap.read()
    if frame is None:
        print('no frame')
        break

    frame = cv.flip(frame,1)
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    key = cv.waitKey(1)
    if key == ord(' '):
        background = frame.copy()
        cv.imshow('background',background)

    cv.imshow('camera',frame)

    if background is not None:
        diff = np.abs(frame.astype(int) - background.astype(int)).astype(np.uint8)
        _,threshold_diff = cv.threshold(diff,30,255,cv.THRESH_BINARY)
        cv.imshow('difference',threshold_diff)
        _,bgs = cv.threshold(diff,50,255,cv.THRESH_BINARY)
        cv.imshow('thresholding',bgs)

    if key == ord('q'):
        break

cap.release()
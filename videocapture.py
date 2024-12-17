import sys
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    sys.exit('No camera available')

while True:
    result,frame = cap.read()
    if frame is None:
        print('no frame')
        break

    cv.imshow('camera',frame)

    key = cv.waitKey(1)

    print(f'Key Code: {key}')

    if key == ord('q') or key == ord('Q'):
        break

    if key == 27:
        break

cap.release()
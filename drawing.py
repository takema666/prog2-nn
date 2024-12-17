import numpy as np
import cv2 as cv
import random

image_width = 640
image_height = 480

while True:
    img = np.zeros((image_height,image_width,3),dtype=np.uint8)

    x1 = int(random.random() * image_width)
    y1 = int(random.random() * image_height)
    x2 = int(random.random() * image_width)
    y2 = int(random.random() * image_height)
    r = int(random.random() * 255)
    g = int(random.random() * 255)
    b = int(random.random() * 255)

    cv.line(img,(x1,y1),(x2,y2),color=(b,g,r),thickness=2)

    cv.imshow('random image',img)

    key = cv.waitKey(1)
    if key == ord(' '):
        break
    elif key == ord('q'):
        break
    elif key == 27:
        break
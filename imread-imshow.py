import sys
import cv2 as cv

image_file = 'non_existent_file.jpg'

print(f'loading image {image_file}...')
img = cv.imread(image_file)
if img is None:
    sys.exit('failed')
else:
    print(f'Image shape: {img.shape}, dtype: {img.dtype}')

cv.imshow('NewWindowTitle',img)

#key = cv.waitKey()

key = cv.waitKey(5000)
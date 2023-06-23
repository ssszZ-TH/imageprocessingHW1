import numpy as np
import cv2 as cv

img_arr = np.zeros([300,300], dtype=np.uint8)

for y in range(150,200):
    for x in range(15,260):
        img_arr[x,y] = 100
    
cv.imshow('spaspa',img_arr)

cv.waitKey(0)
cv.destroyAllWindows()
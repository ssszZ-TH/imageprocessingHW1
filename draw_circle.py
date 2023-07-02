import numpy as np
import cv2 as cv

r = 50
h = 250
k = 250
resolution = 500
sampling_line=500

img_arr = np.zeros([resolution,resolution], dtype=np.uint8)

for y in range(0,resolution):
    for x in range(0,resolution):
        if (x-h)**2 + (y-k)**2 > (r**2) and (x-h)**2 + (y-k)**2 < (r**2)+sampling_line:
            img_arr[x,y]=255
    
cv.imshow('spaspa',img_arr)

cv.waitKey(0)
cv.destroyAllWindows()

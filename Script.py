
import numpy as np
import cv2

#read image
img_src = cv2.imread('image.tiff', cv2.IMREAD_UNCHANGED)

#create filter
s = (3, 3)
kernel = np.ones(s, dtype=int)

#filter the source image
img_rst = cv2.filter2D(img_src, -1, kernel)

#save result image
cv2.imwrite('result.tiff', img_rst, [cv2.IMWRITE_TIFF_COMPRESSION, 1])

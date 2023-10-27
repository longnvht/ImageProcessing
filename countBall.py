
import numpy as np
import cv2

im = cv2.imread('colorfull_ballon.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # chuyển ảnh xám thành ảnh grayscale
thresh = cv2.Canny(imgray, 127, 255) # nhị phân hóa ảnh
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(im, contours, -1, (0, 255, 0), 1) # vẽ lại ảnh contour vào ảnh gốc

# show ảnh lên
cv2.imshow("ballons", im)
cv2.waitKey(0)

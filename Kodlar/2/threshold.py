import cv2
import numpy as np

image = cv2.imread("../images/box_up.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

onemsiz, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.namedWindow("Original", cv2.WINDOW_FREERATIO)
cv2.namedWindow("thresholded image", cv2.WINDOW_FREERATIO)
cv2.imshow("Original", image)
cv2.imshow("thresholded image", thresh)
cv2.waitKey()

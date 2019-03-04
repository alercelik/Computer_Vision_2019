import cv2
import numpy as np

image = cv2.imread('../images/renkler.png')

# lower = (0, 150, 0) # b, g ve r değeleri
# upper = (255, 200, 255) # b, g ve r değeleri
result = cv2.inRange(image, (0, 150, 0), (255, 200, 255))

cv2.imshow("result", result)
cv2.imshow('ORIGINAL', image)
cv2.waitKey()

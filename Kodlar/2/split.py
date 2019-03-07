import cv2
import numpy as np

image = cv2.imread('../images/renkler.png')

# Fotoğraf BGR olduğu için B, G, R diye ayırdık (isimlendirdik).
# Fotoğraf CMY (cyan, magenta, yellow) veya HSV (hue, saturation, value)
# gibi farklı renk uzayına sahip olsaydı o zaman o şekilde isimlendirirdik.
B, G, R = cv2.split(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('ORIGINAL', cv2.WINDOW_FREERATIO)
cv2.namedWindow('B', cv2.WINDOW_FREERATIO)
cv2.namedWindow('G', cv2.WINDOW_FREERATIO)
cv2.namedWindow('R', cv2.WINDOW_FREERATIO)
cv2.namedWindow('grayscale', cv2.WINDOW_FREERATIO)
cv2.imshow('ORIGINAL', image)
cv2.imshow('grayscale', gray)
cv2.imshow('B', B)
cv2.imshow('G', G)
cv2.imshow('R', R)
cv2.waitKey()

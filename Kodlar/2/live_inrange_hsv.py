import cv2
import numpy as np

# 0 -> default camera (genelde dahili webcam)
# usb kameraları için vs. 1, 2 vs..
camera = cv2.VideoCapture(0)

# döngüden çıkmak için terminal üstündeyken ctrl+c yapın.
while True:
	_, frame = camera.read()
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# görüntü HSV renk uzayında olduğu için alt ve üst değeleri
	# HSV formatında ayarlamamız gerekli.
	result = cv2.inRange(hsv_frame, (42, 60, 75), (70, 255, 255))

	cv2.imshow("frame", frame)
	cv2.imshow("result", result)
	# alttaki waitKey bizim işimize yaramasa bile (30 ms bekliyor) gerekli.
	cv2.waitKey(30)

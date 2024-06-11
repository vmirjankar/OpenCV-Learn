import numpy as np
import cv2

cap=cv2.VideoCapture(0) #captures video camera

while True:
	#returns frame (image) and ret which returns true or false
	ret, frame=cap.read()

	width=int(cap.get(3)) #width property of the video frame
	height=int(cap.get(4))

	#HSV: hue, saturation and lightness/brightness
	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_blue=np.array([90,50,50])
	upper_blue=np.array([130,255,255])

	#returns a mask of the image with the specified parameters
	mask=cv2.inRange(hsv, lower_blue, upper_blue) 

	#mask tells us which pixels to keep
	result=cv2.bitwise_and(frame, frame, mask=mask)


	cv2.imshow('frame', result)
	cv2.imshow('mask', mask)

	if cv2.waitKey(1)==ord('q'):
		break

cap.release() #releases video camera
cv2.destroyAllWindows()
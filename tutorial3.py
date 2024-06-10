import numpy as np
import cv2

cap=cv2.VideoCapture(0) #captures video camera

while True:
	#returns frame (image) and ret which returns true or false
	ret, frame=cap.read()

	width=int(cap.get(3)) #width property of the video frame
	height=int(cap.get(4))

	#empty numpy array with all zeros
	image=np.zeros(frame.shape, np.uint8) 

	smaller_frame=cv2.resize(frame,(0,0), fx=0.5, fy=0.5)

	image[:height//2, :width//2]=smaller_frame
	image[height//2:, :width//2]=cv2.rotate(smaller_frame, cv2.ROTATE_180)
	image[:height//2, width//2:]=cv2.rotate(smaller_frame, cv2.ROTATE_180)
	image[height//2:, width//2:]=smaller_frame

	cv2.imshow('frame', image)

	if cv2.waitKey(1)==ord('q'):
		break

cap.release() #releases video camera
cv2.destroyAllWindows()
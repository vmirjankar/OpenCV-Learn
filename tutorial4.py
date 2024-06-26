import numpy as np
import cv2

cap=cv2.VideoCapture(0) #captures video camera

while True:
	#returns frame (image) and ret which returns true or false
	ret, frame=cap.read()
	width=int(cap.get(3)) 
	height=int(cap.get(4))

	#draw a line by specifying coordinates
	#                      SP          EP           color    line thickness
	img = cv2.line(frame, (0,0), (width, height), (255,0,0),      10)
	img = cv2.line(img, (0,height), (width, 0), (0,255,0),      5)

	#rectangle
	#           source img  center    radius    color       LT(-1 to fill)
	img=cv2.rectangle(img, (100,100),(200,200),(128,128,128), 5)

	#circle
	#        source img  center  radius  color   LT(-1 to fill)
	img=cv2.circle(img, (300,300), 60, (0,0,255), -1)

	#text
	font=cv2.FONT_ITALIC
	#          /base img      /text      /bottomleftcorner/font/fScale/color/LT  /lineType
	img=cv2.putText(img, 'Fifa is Great!', (10,height-10), font, 2, (0,0,0), 5, cv2.LINE_AA)

	
	cv2.imshow('frame', img)

	if cv2.waitKey(1)==ord('q'):
		break

cap.release() #releases video camera
cv2.destroyAllWindows()
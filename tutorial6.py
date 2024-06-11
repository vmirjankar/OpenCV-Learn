import numpy as np
import cv2

img=cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#                        source img/no of corners/quality/Min Eucliedean Distance
corners=cv2.goodFeaturesToTrack(gray,     100,      0.01,      10)
corners=np.int0(corners)

for corner in corners:
	x,y=corner.ravel() #flattens the array
	cv2.circle(img, (x,y), 5, (250, 0, 0), -1)

for i in range(len(corners)):
	for j in range(i+1, len(corners)):
		corner1=tuple(corners[i][0])
		corner2=tuple(corners[j][0])
		#1. uses a function to map all the values, 2. returns a new array containing all of the values, 3. convert it into a tuple
		color=tuple(map(lambda x: int (x), np.random.randint(0,255, size=3)))
		cv2.line(img, corner1, corner2, color ,1)



cv2.imshow('Frame', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
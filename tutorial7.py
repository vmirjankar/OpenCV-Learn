import numpy as np
import cv2

#size of base img and template img should be proportional
img=cv2.resize(cv2.imread('assets/soccer_practice.jpg',0),(0,0), fx=0.75, fy=0.75)
template=cv2.resize(cv2.imread('assets/shoe.png',0),(0,0), fx=0.75, fy=0.75)

h,w=template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
	img2=img.copy()

	#performs a convolution: sliding around the template img to match the base img
	result=cv2.matchTemplate(img2,template, method)
	#returns the min val and loc and the max val and loc
	min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(result)
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		location=min_loc
	else:
		location=max_loc

	bottom_right = (location[0]+w, location[1]+h)	
	cv2.rectangle(img2,location,bottom_right, 255,5)

	cv2.imshow('Match',img2)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
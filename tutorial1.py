import cv2

img=cv2.imread('assets/logo.jpg', 1) #read the image
img=cv2.resize(img,(0,0), fx=2, fy=2) #resize the image
img = cv2.rotate(img, cv2.ROTATE_180) #rotate the image

cv2.imwrite('new_img.jpg',img) #write the new image


cv2.imshow('IMAGE',img) #display the image
cv2.waitKey(0) #waits for specified time in seconds for a key 
cv2.destroyAllWindows() #destroys all windows
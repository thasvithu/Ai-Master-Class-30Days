import cv2

img = cv2.imread("photo.png") #Read an img

cv2.imshow('show', img) #to diplay the image

cv2.imwrite("photo.jpg", img)



cv2.waitKey(10000)
cv2.destroyAllWindows()

cv2.waitKey(10000)
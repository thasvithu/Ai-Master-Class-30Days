import cv2

image = cv2.imread("photo.jpg")

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", image)
cv2.imshow("Gray", grayImage)

cv2.imwrite("grayImage", grayImage)

print(image.shape)
print(image.size)

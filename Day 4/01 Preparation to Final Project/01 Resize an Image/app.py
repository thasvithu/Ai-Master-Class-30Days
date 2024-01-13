# Import necessary libraries
import cv2
import imutils

# Read the image from file
img = cv2.imread("photo.jpg")

# Resize the image using the imutils library (width set to 100 pixels)
reSizeImage = imutils.resize(img, width=100)

# Save the resized image to a new file
cv2.imwrite("resizedImage.jpg", reSizeImage)

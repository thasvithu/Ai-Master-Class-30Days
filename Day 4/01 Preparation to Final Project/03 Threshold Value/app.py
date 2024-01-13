# Import the OpenCV library
import cv2

# Read the image from file
img = cv2.imread("photo.jpg")

# Convert the image to grayscale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
# cv2.threshold(src, threshold, maxValueForThreshold, binary, type)
_, thresholdImg = cv2.threshold(grayImg, 180, 255, cv2.THRESH_BINARY)

# Display the original and threshold images
cv2.imshow("Original", img)
cv2.imshow("Threshold Image", thresholdImg)

# Save the threshold image to a new file
cv2.imwrite("threshold.jpg", thresholdImg)

# Black - 0
# 180
# White - 255

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

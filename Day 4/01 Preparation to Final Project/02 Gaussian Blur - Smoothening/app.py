# Import the OpenCV library
import cv2

# Read the image from file
img = cv2.imread("photo.jpg")

# Apply GaussianBlur with a large kernel and high borderType
gaussianImg = cv2.GaussianBlur(img, (41, 41), 50)

# Apply GaussianBlur with a smaller kernel and borderType set to 0
gaussianImg1 = cv2.GaussianBlur(img, (21, 21), 0)

# Display the original and GaussianBlur images
cv2.imshow("Original", img)
cv2.imshow("GaussianBlur", gaussianImg)
cv2.imshow("GaussianBlur1", gaussianImg1)

# Save the GaussianBlur images to new files
cv2.imwrite("GaussianBlur.jpg", gaussianImg)
cv2.imwrite("GaussianBlur1.jpg", gaussianImg1)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

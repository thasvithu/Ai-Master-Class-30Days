# Import the OpenCV library
import cv2

# Read the image from file
image = cv2.imread("photo.jpg")

# Convert the image to grayscale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale images
cv2.imshow("Original", image)
cv2.imshow("Gray", grayImage)

# Save the grayscale image to a new file
cv2.imwrite("grayImage.jpg", grayImage)

# Print the shape and size of the original image
print("Original Image Shape:", image.shape)
print("Original Image Size:", image.size)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

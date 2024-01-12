# Author: @vithusan
# Description: Motion detection using OpenCV

import cv2
import time
import imutils

# Open the camera (0 indicates the default camera)
cam = cv2.VideoCapture(0)
time.sleep(1)  # Allow the camera to warm up

firstframe = None  # Variable to store the first frame for comparison
area = 500  # Minimum contour area to consider as a moving object

while True:
    _, img = cam.read()  # Read a frame from the camera
    text = "Normal"  # Default text

    img = imutils.resize(img, width=1000)  # Resize the frame for better processing speed
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale

    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)  # Apply Gaussian blur for smoother results

    # If it's the first frame, store it and continue to the next iteration
    if firstframe is None:
        firstframe = gaussianImg
        continue

    # Compute the absolute difference between the current frame and the first frame
    imgDiff = cv2.absdiff(firstframe, gaussianImg)

    # Apply a binary threshold to the difference image
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]

    # Dilate the thresholded image to fill gaps in contours
    threshImg = cv2.dilate(threshImg, None, iterations=2)

    # Find contours in the thresholded image
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Loop over the contours
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving object detected"

    # Display the text on the frame
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Show the frame with the bounding boxes
    cv2.imshow("cameraFeed", img)

    key = cv2.waitKey(10)  # Wait for a key event
    if key == ord("q"):  # If 'q' is pressed, break out of the loop
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()

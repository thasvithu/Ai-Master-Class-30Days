import imutils
import cv2

# Define the HSV color range for object tracking
readLower = (95, 49, 100)
readUpper = (154, 255, 255)


# Open the camera
camera = cv2.VideoCapture(0)

while True:
    # Read the frame from the camera
    (grabbed, frame) = camera.read()

    # Resize the frame for faster processing
    frame = imutils.resize(frame, width=1000)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # Create a mask to filter out the specified color range
    mask = cv2.inRange(hsv, readLower, readUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours in the mask
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    center = None

    # Check if contours are found
    if len(cnts) > 0:
        # Find the largest contour
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        
        # Calculate the center of the contour
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # Draw a circle around the object if it's large enough
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            # Perform actions based on the position and size of the object
            if radius > 250:
                print("Stop")
            else:
                if center[0] < 150:
                    print("Right")
                elif center[0] > 450:
                    print("Left")
                elif radius < 250:
                    print("Front")
                else:
                    print("Stop")

    # Display the frame
    cv2.imshow("Frame", frame)

    # Check for the 'q' key to exit the loop
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()

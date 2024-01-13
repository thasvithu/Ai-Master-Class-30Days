import cv2

# Path to the Haar Cascade XML file
alg = "haarcascade_frontalface_default.xml"

# Loading the Haar Cascade classifier
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + alg)

# Camera ID initialization (assuming 0 for the default camera, change it if needed)
cam = cv2.VideoCapture(0)

while True:
    # Reading a frame from the camera
    _, img = cam.read()

    # Converting color image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecting faces
    faces = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=4)

    # Drawing rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Displaying the result
    cv2.imshow("Face Detection", img)

    # Checking for the 'ESC' key to exit the loop
    key = cv2.waitKey(10)
    if key == 27:
        break

# Releasing the camera and closing all windows
cam.release()
cv2.destroyAllWindows()

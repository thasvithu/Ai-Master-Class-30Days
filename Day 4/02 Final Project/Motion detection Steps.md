**Moving Object Detection using OpenCV**

**Project Overview:**
- **Objective:** Detect moving objects in a video feed using OpenCV.
- **Tools Used:** Python, OpenCV.
- **Author:** @vithusan.

**Key Steps:**
1. **Import Libraries:**
   - Import necessary libraries like `cv2`, `time`, and `imutils`.

2. **Setup Camera:**
   - Use `cv2.VideoCapture(0)` to access the default camera (change the argument for a different camera).
   - Allow the camera to warm up with `time.sleep(1)`.

3. **Capture First Frame:**
   - Capture the first frame as a reference for comparison.

4. **Motion Detection Loop:**
   - Continuously capture frames from the camera.
   - Resize frames for better processing using `imutils.resize`.
   - Convert frames to grayscale and apply Gaussian blur.

5. **Compute Difference:**
   - Compute the absolute difference between the current frame and the first frame.

6. **Thresholding:**
   - Apply binary thresholding to the difference image.

7. **Dilation:**
   - Dilate the thresholded image to fill gaps in contours.

8. **Find Contours:**
   - Find contours in the thresholded image.

9. **Object Detection:**
   - Loop over the contours and draw bounding boxes around moving objects.
   - Set a minimum contour area to filter out small movements.

10. **Display Results:**
    - Display the original frame with bounding boxes and text indicating motion.

11. **Key Controls:**
    - Press 'q' to exit the application.
  
**Project Completion Criteria:**
- Successful detection and tracking of moving objects in the video feed.
- Clean and well-documented code.
- Optimal performance under different scenarios.
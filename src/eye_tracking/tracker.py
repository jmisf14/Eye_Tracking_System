import cv2
import numpy as np

class EyeTracker:
    def __init__(self):
        self.tracking = False

    def start_tracking(self):
        self.tracking = True

    def get_gaze_direction(self, frame, eyes):
        """
        Calculate the gaze direction based on the detected eyes.

        Args:
            frame (numpy.ndarray): The current video frame.
            eyes (list): List of bounding boxes for detected eyes [(x, y, w, h), ...].

        Returns:
            tuple: Normalized gaze direction (x, y) or None if gaze cannot be determined.
        """
        if not self.tracking or not eyes:
            return None

        # Use the first detected eye for simplicity
        eye = eyes[0]
        x, y, w, h = eye

        # Extract the eye region of interest (ROI)
        eye_roi = frame[y:y+h, x:x+w]
        gray_eye = cv2.cvtColor(eye_roi, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to detect the pupil
        _, threshold_eye = cv2.threshold(gray_eye, 50, 255, cv2.THRESH_BINARY_INV)

        # Debug: Display the thresholded eye
        cv2.imshow("Thresholded Eye", threshold_eye)

        # Find contours in the thresholded eye region
        contours, _ = cv2.findContours(threshold_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Find the largest contour, assuming it's the pupil
            largest_contour = max(contours, key=cv2.contourArea)
            (cx, cy), radius = cv2.minEnclosingCircle(largest_contour)

            # Debug: Print pupil position and radius
            #print(f"Pupil Position: ({cx}, {cy}), Radius: {radius}")

            # Normalize the pupil position to the eye region
            normalized_x = cx / w
            normalized_y = cy / h

            # Return the normalized gaze direction
            return (normalized_x, normalized_y)

        # If no pupil is detected, return None
        return None
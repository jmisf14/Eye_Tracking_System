# filepath: c:\Users\adria\OneDrive\IE_University\Year3\AI COMPUTER VISION\eye-tracking-project\src\screen_capture.py
import mss
import numpy as np
import cv2

def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img
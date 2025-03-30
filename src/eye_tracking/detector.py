import cv2

class EyeDetector:
    def __init__(self, face_cascade_path, eye_cascade_path):
        self.face_cascade = cv2.CascadeClassifier(face_cascade_path)
        self.eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

    def detect_faces(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

        # Debug: Print detected faces
        # print(f"Detected Faces: {faces}")

        return faces

    def detect_eyes(self, frame, face_coordinates):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = []
        for (x, y, w, h) in face_coordinates:
            roi_gray = gray_frame[y:y+h, x:x+w]
            detected_eyes = self.eye_cascade.detectMultiScale(roi_gray)

            # Debug: Print detected eyes for each face
            # print(f"Detected Eyes in Face Region ({x}, {y}, {w}, {h}): {detected_eyes}")

            # Adjust eye coordinates to the full frame
            eyes.extend([(x + ex, y + ey, ew, eh) for (ex, ey, ew, eh) in detected_eyes])

        # Debug: Print all detected eyes
        # print(f"All Detected Eyes: {eyes}")

        return eyes
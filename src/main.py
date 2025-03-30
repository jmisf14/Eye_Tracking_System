import cv2
import mediapipe as mp
import numpy as np
import pyautogui  

def main():
    # Initialize MediaPipe Face Mesh
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, max_num_faces=1)
    drawing_utils = mp.solutions.drawing_utils

    # Start video capture
    cap = cv2.VideoCapture(0)

    screen_width, screen_height = 1920, 1080  # Screen dimensions for gaze normalization

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe Face Mesh
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Draw face landmarks for visualization (optional)
                drawing_utils.draw_landmarks(
                    frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                    drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                    drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=1, circle_radius=1)
                )

                # Extract eye landmarks
                left_eye = [face_landmarks.landmark[i] for i in [33, 133, 160, 159, 158, 144, 153, 154, 155]]
                right_eye = [face_landmarks.landmark[i] for i in [362, 263, 387, 386, 385, 373, 380, 374, 381]]

                # Calculate gaze direction (simplified example)
                left_eye_center = np.mean([[p.x, p.y] for p in left_eye], axis=0)
                right_eye_center = np.mean([[p.x, p.y] for p in right_eye], axis=0)
                gaze_x = int(screen_width * (left_eye_center[0] + right_eye_center[0]) / 2)
                gaze_y = int(screen_height * (left_eye_center[1] + right_eye_center[1]) / 2)

                # Visualize the gaze point on the video feed
                cv2.circle(frame, (gaze_x, gaze_y), 10, (0, 255, 0), -1)
                print(f"Gaze Coordinates: ({gaze_x}, {gaze_y})")  # Log gaze coordinates

                # Display a red dot on the screen at the gaze coordinates
                pyautogui.moveTo(gaze_x, gaze_y)

        # Display the frame
        cv2.imshow('Eye Tracking', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
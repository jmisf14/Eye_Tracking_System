def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def preprocess_frame(frame):
    import cv2
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized_frame = cv2.resize(gray_frame, (640, 480))
    return resized_frame
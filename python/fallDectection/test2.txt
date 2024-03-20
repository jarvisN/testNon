import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose model.
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(p1, p2, p3):
    """Calculates the angle formed by three points: p1, p2, and p3.
    p1 is the first point, p2 is the vertex point where the angle is to be calculated, and p3 is the third point."""
    vector_1 = np.array([p1['x'] - p2['x'], p1['y'] - p2['y']])
    vector_2 = np.array([p3['x'] - p2['x'], p3['y'] - p2['y']])
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product) * 180 / np.pi
    return angle

def detect_fall(pose_landmarks):
    """Detects fall from MediaPipe Pose landmarks."""
    if pose_landmarks:
        # Convert landmarks to dictionary
        shoulder = {'x': pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x, 'y': pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y}
        hip = {'x': pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x, 'y': pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y}
        knee = {'x': pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].x, 'y': pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y}

        # Calculate the angle
        angle = calculate_angle(shoulder, hip, knee)
        
        # Fall detection: if the angle is not close to 180 degrees (straight line)
        print(f"debug : {angle}")
        if angle < 150 or angle > 200:
            return True
    return False

def detect_pose(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)
    
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    return frame, results.pose_landmarks

def capture_frames():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame") 
            break

        frame, pose_landmarks = detect_pose(frame)

        if pose_landmarks and detect_fall(pose_landmarks):
            cv2.putText(frame, "Fall Detected!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('MediaPipe Pose', frame)
        
        if cv2.waitKey(5) & 0xFF == 27:  # Press ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_frames()

import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose model.
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(p1, p2):
    """คำนวณมุมระหว่างสองจุด p1 และ p2 กับแนวนอน"""
    angle = np.arctan2(p2['y'] - p1['y'], p2['x'] - p1['x']) * 180 / np.pi
    return angle

def calculate_vector_angle(p1, p2):
    """คำนวณมุมระหว่างเวกเตอร์ของสองจุดกับแนวนอน"""
    vector = [p2['x'] - p1['x'], p2['y'] - p1['y']]
    norm_vector = np.sqrt(vector[0]**2 + vector[1]**2)
    unit_vector = [vector[0] / norm_vector, vector[1] / norm_vector]
    angle = np.arccos(unit_vector[0]) * 180 / np.pi  # เวกเตอร์กับแนวนอน
    return angle


def detect_fall(pose_landmarks):
    """ตรวจจับการล้มจาก landmarks ของ MediaPipe Pose"""
    # แปลงข้อมูล landmarks เป็น dictionary
    shoulder = {'x': pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x, 'y': pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y}
    hip = {'x': pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x, 'y': pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y}
    knee = {'x': pose_landmarks[mp_pose.PoseLandmark.LEFT_KNEE].x,'y':pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y}
    # คำนวณมุม
    angle = calculate_angle(shoulder, hip)
    # angle = calculate_vector_angle(shoulder,hip)
    
    # ตรวจจับการล้ม: ถ้ามุมใกล้เคียงกับแนวนอน (90 หรือ -90 องศา)
    if angle > 75 or angle < -75:
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
        
        if cv2.waitKey(5) & 0xFF == 27 :  # Press ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_frames()

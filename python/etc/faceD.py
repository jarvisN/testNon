import cv2
import dlib
import numpy as np

# โหลดตัวตรวจจับใบหน้าและโมเดลจุดสำคัญบนใบหน้า
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# ฟังก์ชั่นเพื่อคำนวณอัตราส่วนตา
def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# ฟังก์ชั่นเพื่อคำนวณอัตราส่วนปาก
def mouth_aspect_ratio(mouth):
    A = np.linalg.norm(mouth[14] - mouth[18])
    B = np.linalg.norm(mouth[12] - mouth[16])
    mar = A / B
    return mar

# รับวิดีโอจากกล้อง
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        # ตรวจจับตาและคำนวณ EAR
        left_eye = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(36, 42)])
        right_eye = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(42, 48)])
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        
        # ตรวจจับปากและคำนวณ MAR
        mouth = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(48, 68)])
        mar = mouth_aspect_ratio(mouth)

        # ใช้ค่า EAR และ MAR เพื่อตรวจจับการหลับตาหรือการอ้าปาก

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

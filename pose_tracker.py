import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

def run_squat():
    pose = mp_pose.Pose()
    cap = cv2.VideoCapture(0)
    count, direction = 0, 0
    feedback = "Fix your form"

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

            angle = calculate_angle(hip, knee, ankle)

            if angle > 160:
                feedback = "Stand up"
                if direction == 1:
                    count += 1
                    direction = 0
            elif angle < 90:
                feedback = "Squat down"
                direction = 1
            else:
                feedback = "Keep your form"

            mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.putText(frame, f'Reps: {count}', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 4)
            cv2.putText(frame, feedback, (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 3)

        cv2.imshow('Squat Counter', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def run_pushup():
    pose = mp_pose.Pose()
    cap = cv2.VideoCapture(0)
    count, direction = 0, 0
    feedback = "Fix your form"

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            angle = calculate_angle(shoulder, elbow, wrist)

            if angle > 150:
                feedback = "Up"
                if direction == 1:
                    count += 1
                    direction = 0
            elif angle < 70:
                feedback = "Down"
                direction = 1
            else:
                feedback = "Keep your form"

            mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.putText(frame, f'Reps: {count}', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 4)
            cv2.putText(frame, feedback, (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 3)

        cv2.imshow('Pushup Counter', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def run_bicep_curl():
    pose = mp_pose.Pose()
    cap = cv2.VideoCapture(0)
    count, direction = 0, 0
    feedback = "Fix your form"

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            angle = calculate_angle(shoulder, elbow, wrist)

            if angle > 150:
                feedback = "Extend"
                if direction == 1:
                    count += 1
                    direction = 0
            elif angle < 40:
                feedback = "Curl"
                direction = 1
            else:
                feedback = "Keep your form"

            mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.putText(frame, f'Reps: {count}', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 4)
            cv2.putText(frame, feedback, (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 3)

        cv2.imshow('Bicep Curl Counter', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def start_exercise(exercise_name):
    if exercise_name == "squat":
        run_squat()
    elif exercise_name == "pushup":
        run_pushup()
    elif exercise_name == "bicep_curl":
        run_bicep_curl()
    else:
        print("Invalid exercise name.")

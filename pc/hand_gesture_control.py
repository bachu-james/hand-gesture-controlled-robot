import cv2
import mediapipe as mp
import socket
import time

# === ESP32 Network Settings ===
ESP32_IP = "192.168.1.100"  # change to your ESP32 IP
ESP32_PORT = 8888
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# === Initialize MediaPipe Hands ===
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# === Finger mapping to car commands ===
COMMANDS = {
    0: "STOP",
    1: "FORWARD",
    2: "BACKWARD",
    3: "LEFT",
    4: "RIGHT",
    5: "STOP"
}

# === Function to count fingers ===
def count_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Little
    finger_pips = [6, 10, 14, 18]
    fingers = 0

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers += 1

    # Other fingers
    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            fingers += 1

    return fingers

# === Start Camera ===
cap = cv2.VideoCapture(0)
last_cmd = None
last_sent = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    finger_count = 0
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            finger_count = count_fingers(hand_landmarks)
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cmd = COMMANDS.get(finger_count, "STOP")

    cv2.putText(frame, f"Fingers: {finger_count}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(frame, f"Command: {cmd}", (30, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Control", frame)

    # Send UDP command only when changed or every 1 second
    now = time.time()
    if cmd != last_cmd or (now - last_sent) > 1:
        sock.sendto(cmd.encode(), (ESP32_IP, ESP32_PORT))
        print(f"Sent: {cmd}")
        last_cmd = cmd
        last_sent = now

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
sock.close()


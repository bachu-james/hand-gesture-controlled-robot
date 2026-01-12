# Gesture Controlled Robot using ESP32, MediaPipe & OpenCV

This project demonstrates a **gesture-controlled robot** where **hand gestures are detected on a PC using MediaPipe and OpenCV**, and the control commands are sent wirelessly to an **ESP32-based robot**.

The system enables **real-time human–robot interaction** using computer vision without any wearable sensors.

---

## 🔧 Hardware

* ESP32 development board
* Robot chassis (DC motors / BO motors)
* Motor driver (L298N / L293D)
* Power supply (battery)
* PC / Laptop with webcam

---

## 💻 Software

* Python 3
* OpenCV
* MediaPipe
* ESP32 Arduino Core
* Arduino IDE / PlatformIO

---

## ✨ Features

* Real-time hand gesture detection using webcam
* MediaPipe-based hand landmark tracking
* Gesture-to-motion mapping (Forward / Backward / Left / Right / Stop)
* Wireless communication between PC and ESP32
* Low-latency robot control

---

## ▶️ Demo Video

🎥 **Working Demo (YouTube Shorts):**
👉 [https://youtube.com/shorts/V_CBfRjom3w](https://youtube.com/shorts/V_CBfRjom3w)

This video shows the **gesture-controlled robot in action**, where hand gestures detected on the PC using **MediaPipe + OpenCV** control the robot powered by **ESP32**.

---

## 🧠 System Architecture

1. Webcam captures hand gestures on PC
2. MediaPipe extracts hand landmarks
3. OpenCV processes and classifies gestures
4. Control commands sent to ESP32 (Wi-Fi / Bluetooth)
5. ESP32 drives motors via motor driver

---

## 🚀 How It Works

* Hand gestures are recognized based on finger positions
* Each gesture is mapped to a specific robot movement
* ESP32 receives commands and controls motors accordingly

---

## 📌 Notes

* Ensure stable lighting for accurate gesture detection
* Adjust MediaPipe confidence thresholds if needed
* Tune motor speed values for smoother movement

---

## 🔮 Future Improvements

* Add obstacle avoidance
* Use ROS 2 for scalability
* Add gesture-based speed control
* Mobile app integration

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License

MIT License

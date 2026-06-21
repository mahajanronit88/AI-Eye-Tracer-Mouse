# AI Eye-Tracking Virtual Mouse 👁️🖱️

An innovative Python application that allows users to control their computer mouse cursor using eye movements and perform clicks by blinking. This project utilizes computer vision to track iris movements in real-time.

## 🚀 Features
- **Hands-Free Navigation:** Move the mouse cursor by just looking around the screen.
- **Blink-to-Click:** Automatic left-click detection when you blink your left eye.
- **Dynamic Smoothing:** Linear interpolation (LERP) implemented to reduce cursor shaking/jittering.
- **Failsafe Disabled:** Smooth edge-to-edge screen navigation without abrupt crashes.

## 🛠️ Tech Stack
- **Python**
- **OpenCV** (Image processing & webcam feed)
- **MediaPipe** (Face Mesh & Iris landmark detection)
- **PyAutoGUI** (Programmatic mouse control)

## 📦 Installation & Setup

1. Clone this repository:
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME<img width="640" height="480" alt="Mouse controller with eyess1" src="https://github.com/user-attachments/assets/addb167a-d830-469c-bf66-f2042ec250d3" />

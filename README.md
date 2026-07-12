# 🎯 FocusLens

## AI-Powered Study Environment Analyzer

FocusLens is a real-time Computer Vision application that helps students analyze their study environment using Artificial Intelligence.

The application detects study-related objects through a webcam, evaluates the user's study environment, calculates a focus score, tracks study sessions, and generates personalized recommendations to encourage distraction-free learning.

---

## 📌 Problem Statement

Students often lose concentration due to distractions such as mobile phones while studying. Existing object detection systems can identify objects but do not provide meaningful analysis of study behavior.

FocusLens addresses this problem by combining real-time object detection with a custom focus analysis engine to provide intelligent feedback on a student's study environment.

---

## 🎯 Objectives

- Detect study-related objects using Computer Vision.
- Analyze the student's study environment.
- Calculate a Focus Score based on detected objects.
- Track study session duration.
- Monitor phone usage during study sessions.
- Generate recommendations to improve concentration.
- Export a study report for future analysis.

---

## ✨ Features

- 🎥 Real-time webcam-based object detection
- 🧠 AI-powered study environment analysis
- 📊 Dynamic Focus Score calculation
- ⏱️ Live study session timer
- 📱 Phone usage tracking
- 🚨 Distraction counter
- 💡 Intelligent study recommendations
- 📄 One-click study report generation
- 🖥️ Interactive real-time dashboard
- 📂 Modular software architecture for maintainability

---

## 🛠️ Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.11 |
| Computer Vision | OpenCV |
| Object Detection | YOLOv8 Nano (Ultralytics) |
| Deep Learning Framework | PyTorch |
| Image Processing | OpenCV |
| User Interface | OpenCV Drawing API |
| Development Environment | Visual Studio Code |

---

## 📂 Project Structure

```text
FocusLens/
│
├── app.py
│
├── core/
│   ├── detector.py
│   ├── analyzer.py
│   ├── dashboard.py
│   ├── session.py
│   └── report.py
│
├── assets/
├── docs/
├── models/
├── outputs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ How FocusLens Works

The application follows a modular pipeline where each component performs a single responsibility.

```text
Webcam
   │
   ▼
YOLOv8 Object Detection
   │
   ▼
Object Detector
(detector.py)
   │
   ▼
Focus Analyzer
(analyzer.py)
   │
   ▼
Study Session Tracker
(session.py)
   │
   ▼
Dashboard & Report Generator
(dashboard.py + report.py)
```

### Workflow

1. The webcam captures live video frames.
2. YOLOv8 detects study-related objects such as:
   - Person
   - Cell Phone
   - Book
3. The Focus Analyzer evaluates the detected objects and calculates a weighted Focus Score.
4. The Session Tracker monitors:
   - Study duration
   - Phone usage time
   - Number of distractions
5. The Dashboard displays all analytics in real time.
6. The user can press **S** to generate a Study Report inside the `outputs/` folder.

---

## 📐 Focus Score Calculation

FocusLens uses a simple weighted scoring algorithm to estimate the quality of the study environment.

| Condition | Weight |
|-----------|-------:|
| Person Detected | +60 |
| Book Detected | +20 |
| Phone Detected | -30 |

The maximum possible score is **80**.

The final Focus Score is normalized using:

```
Focus Score (%) = (Raw Score / 80) × 100
```

This score is then categorized as:

| Score | Level |
|--------|--------|
| 80–100% | Excellent |
| 60–79% | Focused |
| 30–59% | Needs Attention |
| 0–29% | Distracted |

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_LINK>
```

### 2. Navigate to the Project Folder

```bash
cd FocusLens
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the application using:

```bash
python app.py
```

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **S** | Save Study Report |
| **Q** | Quit Application |

---

## 📊 Results

The application performs the following tasks in real time:

- Detects study-related objects using YOLOv8.
- Calculates a Focus Score.
- Tracks study session duration.
- Monitors phone usage.
- Counts distraction events.
- Displays live analytics through the dashboard.
- Generates a study report on demand.

Example output:

- Study Status : ACTIVE
- Focus Score : 75%
- Session Time : 05:42
- Phone Usage : 00:18
- Distractions : 2

---

## 🔮 Future Scope

Future improvements for FocusLens include:

- Face direction and gaze estimation.
- Eye closure detection for drowsiness.
- Emotion and stress analysis.
- Focus trend graphs over time.
- Cloud synchronization of study reports.
- Personalized productivity insights.
- Mobile application integration.
- Voice-based notifications.

---

## 📚 References

- Ultralytics YOLOv8 Documentation
- OpenCV Documentation
- Python 3.11 Documentation
- PyTorch Documentation
- Microsoft COCO Dataset (pre-trained YOLOv8 model)

---

## 👥 Team

**Team Name:** VisionForge

**HackZen 2026 Open Challenge Submission**

**Project Title:** FocusLens – AI Powered Study Environment Analyzer

### Team Members

| Name | Role |
|------|------|
| Praveen R | Team Leader |
| Jaisurya S | Team Member |
| Mahileshwaran P | Team Member |
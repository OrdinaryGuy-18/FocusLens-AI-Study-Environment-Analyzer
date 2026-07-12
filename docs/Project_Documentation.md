# FocusLens

## AI Powered Study Environment Analyzer

### HackZen 2026 Open Challenge

---

## Team Name

**VisionForge**

---

## Team Members

| Name | Role |
|------|------|
| Praveen R | Team Leader |
| Jaisurya S | Team Member |
| Mahileshwaran P | Team Member |

---

## Project Domain

Computer Vision

---

## Duration

HackZen 2026 Open Challenge

12 July 2026 – 13 July 2026

# 1. Problem Statement

Students often face distractions while studying, especially due to smartphones and other non-study activities. Although object detection technology can identify objects present in an environment, it does not analyze whether the environment is suitable for productive studying.

There is a need for an intelligent Computer Vision system that can observe a student's study environment, evaluate focus-related factors, and provide meaningful feedback to improve study habits.

# 2. Objectives

The objectives of FocusLens are:

- Develop a real-time Computer Vision application using Python and OpenCV.
- Detect study-related objects using the YOLOv8 object detection model.
- Analyze the study environment using a weighted focus scoring system.
- Monitor session duration and distraction events.
- Track phone usage during study sessions.
- Provide real-time recommendations to improve focus.
- Generate a study report summarizing the session.

# 3. Proposed Solution

FocusLens is an AI-powered study environment analyzer that combines real-time object detection with custom analytical logic.

The webcam continuously captures video frames, and the YOLOv8 Nano model detects relevant objects such as people, books, and mobile phones. Based on these detections, the application calculates a focus score, tracks study sessions, records distractions, and provides live recommendations through an interactive dashboard.

The user can also export a study report summarizing the session statistics.

# 4. Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming Language |
| OpenCV | Webcam Capture & Image Processing |
| Ultralytics YOLOv8 Nano | Object Detection |
| PyTorch | Deep Learning Backend |
| Visual Studio Code | Development Environment |

# 5. Dataset

FocusLens uses the pre-trained YOLOv8 Nano model provided by Ultralytics.

The model has been trained on the Microsoft COCO (Common Objects in Context) dataset, which contains 80 object categories, including:

- Person
- Cell Phone
- Book
- Laptop
- Chair
- Bottle

No additional custom dataset was used for this project.

# 6. Methodology

The application follows a modular architecture.

```
Webcam
   │
   ▼
YOLOv8 Nano
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
Dashboard
(dashboard.py)
   │
   ▼
Study Report Generator
(report.py)
```

### Workflow

1. Capture live webcam frames.
2. Detect study-related objects using YOLOv8 Nano.
3. Extract detected object labels.
4. Calculate a weighted focus score.
5. Track session duration and phone usage.
6. Display analytics on the dashboard.
7. Generate a study report when requested.

# 7. Installation & Setup

## Prerequisites

- Python 3.11 or later
- Webcam
- Visual Studio Code (recommended)

## Installation Steps

1. Clone the repository.
2. Create a Python virtual environment.
3. Activate the virtual environment.
4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python app.py
```

The application will automatically initialize the webcam and start detecting objects.

# 8. Usage Instructions

1. Launch the application using `python app.py`.
2. Position yourself in front of the webcam.
3. Allow the system to detect study-related objects.
4. Observe the real-time dashboard displaying:
   - Study Status
   - Focus Score
   - Focus Level
   - Session Duration
   - Phone Usage
   - Distraction Count
5. Press **S** to save a study report.
6. Press **Q** to exit the application.

# 9. Results & Outputs

The developed application successfully performs real-time study environment analysis using Computer Vision.

### Features Demonstrated

- Real-time object detection
- Focus score calculation
- Session tracking
- Phone usage monitoring
- Distraction counting
- Live dashboard visualization
- Study report generation

### Sample Outputs

The generated study report contains:

- Study Status
- Focus Score
- Focus Level
- Session Duration
- Phone Usage
- Number of Distractions
- Recommendation

# 10. Future Scope

Possible future improvements include:

- Eye gaze estimation
- Head pose estimation
- Blink detection
- Drowsiness detection
- Face recognition for personalized reports
- Focus trend visualization
- Cloud storage for study reports
- Mobile application support
- AI-based personalized study recommendations

# 11. References

1. Ultralytics YOLOv8 Documentation
2. OpenCV Documentation
3. Python Documentation
4. PyTorch Documentation
5. Microsoft COCO Dataset


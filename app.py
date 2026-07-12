import cv2
from core.analyzer import FocusAnalyzer
from core.detector import ObjectDetector
from core.dashboard import Dashboard
from core.session import StudySession
from core.report import ReportGenerator

# Initialize objects
detector = ObjectDetector()
analyzer = FocusAnalyzer()
session = StudySession()
dashboard = Dashboard()
report_generator = ReportGenerator()

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening webcam.")
    exit()

print("FocusLens Started")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (1280, 720))

    results, detected_objects = detector.detect(frame)
    analysis = analyzer.analyze(detected_objects)
    analysis = session.update(analysis)

    annotated_frame = results[0].plot()

    annotated_frame = dashboard.draw(
        annotated_frame,
        analysis
    )

    cv2.namedWindow("FocusLens", cv2.WINDOW_NORMAL)

    cv2.imshow("FocusLens", annotated_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        filename = report_generator.save(analysis)
        print(f"\nStudy report saved to: {filename}")
        
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
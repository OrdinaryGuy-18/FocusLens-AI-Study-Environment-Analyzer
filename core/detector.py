from ultralytics import YOLO


class ObjectDetector:
    def __init__(self):
        # Load the YOLOv8 Nano model
        self.model = YOLO("models/yolov8n.pt")

    def detect(self, frame):
        """
        Runs object detection on a frame.

        Returns:
            results -> YOLO result object
            detected_objects -> list of detected object names
        """

        results = self.model(frame, verbose=False)

        detected_objects = []

        for box in results[0].boxes:
            class_id = int(box.cls[0])
            class_name = self.model.names[class_id]
            detected_objects.append(class_name)

        return results, detected_objects
from ultralytics import YOLO

# Initialize the model
model = YOLO('yolov8n.yaml')

# Train the model
model.train(data='dataset.yaml', epochs=50, imgsz=640)

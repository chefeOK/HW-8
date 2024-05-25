import cv2

# Load the trained model
model = YOLO('best.pt')

# Read the video
video_path = 'test_video.mp4'
cap = cv2.VideoCapture(video_path)

# Video writer to save the output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)
    for result in results:
        boxes = result.boxes.data.cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2, score, class_id = box
            label = f'{model.names[int(class_id)]} {score:.2f}'
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255,0,0), 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

    # Write the frame with detections
    out.write(frame)

cap.release()
out.release()

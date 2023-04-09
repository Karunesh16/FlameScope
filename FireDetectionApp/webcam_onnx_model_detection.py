import cv2
import alert_mail
import alert_phone
from PIL import Image
import numpy as np
import datetime

from . import YOLOv8

# pip install -r requirements.txt


# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize YOLOv8 object detector
model_path = "models/best.onnx"
yolov8_detector = YOLOv8.YOLOv8class(model_path, conf_thres=0.5, iou_thres=0.5)


c=0

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
while cap.isOpened():
    # Read frame from the videoq
    ret, frame = cap.read()

    if not ret:
        break

    # Update object localizer
    boxes, scores, class_ids = yolov8_detector(frame)
        
    combined_img = yolov8_detector.draw_detections(frame)
    cv2.imshow("Detected Objects", combined_img)


    
    print(boxes, scores, len(class_ids))
    if len(class_ids) == 1:
        c = c + 1
        # alert.email_alert("Tesqt1","Hello World","karunesh.b@somaiya.edu")
        
    if (c == 15):
        
        img = Image.fromarray(combined_img)
        # img.show()
        img.save("fire_image.jpeg")
        
        c=0
        meassage = f""" Fire Detected
        At Adress : Home/Office, 408, abc apt, Sector 20, Mumbai....
        date: {datetime.datetime.now()} """
        alert_mail.email_alert("FIRE DETECTED!!!!",meassage,"karunesh.b@somaiya.edu")
        alert_phone.call_alert()
    # print(type(combined_img))


    # Press key q to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
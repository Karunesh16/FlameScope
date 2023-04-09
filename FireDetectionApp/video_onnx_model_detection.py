import cv2
import alert_mail
import alert_phone
from PIL import Image
import numpy as np
import datetime
from cap_from_youtube import cap_from_youtube

from yolov8.YOLOv8 import YOLOv8

# pip install -r requirements.txt

# Initialize video
cap = cv2.VideoCapture("input2-original.mp4")


# videoUrl = 'https://youtu.be/Snyg0RqpVxY'
# cap = cap_from_youtube(videoUrl, resolution='720p')
# start_time = 5 # skip first {start_time} seconds
# cap.set(cv2.CAP_PROP_POS_FRAMES, start_time * cap.get(cv2.CAP_PROP_FPS))

# out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), cap.get(cv2.CAP_PROP_FPS), (3840, 2160))


# Initialize YOLOv8 model
model_path = "models/best.onnx"
yolov8_detector = YOLOv8(model_path, conf_thres=0.5, iou_thres=0.5)



c=0

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
while cap.isOpened():

    # Press key q to stop
    if cv2.waitKey(1) == ord('q'):
        break

    try:
        # Read frame from the video
        ret, frame = cap.read()
        if not ret:
            break
    except Exception as e:
        print(e)
        continue

    # Update object localizer
    boxes, scores, class_ids = yolov8_detector(frame)

    combined_img = yolov8_detector.draw_detections(frame)
    cv2.imshow("Detected Objects", combined_img)
    # out.write(combined_img)

    #Alert block
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
    
    
# out.release()